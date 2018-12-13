from app.forms.book import DriftForm
from app.service.drift import DriftService
from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.wish import Wish
from app.view_models.drift import DriftViewModel
from flask import render_template, flash, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from sqlalchemy import or_, desc
from app import cache

from . import web
from app.models.gift import Gift

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    # filter_by(id=gid, launched=True)没有下面这条语句好。下面的语句可以多判断一种状态
    current_gift = Gift.query.get_or_404(gid)
    # if current_gift.launched:
    #     flash('这本书正处于交易状态，暂时不可以索要')
    #     return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^, 不能向自己索要书籍噢')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    can = current_user.can_satisfied_wish()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    drift_form = DriftForm(request.form)
    if request.method == 'POST':
        if drift_form.validate():
            DriftService.save_a_drift(drift_form, current_gift)
            # flash(drift_form.errors, category='drift_form_error')
            # else:
            # 反范式设计，会存储一部分冗余信息。
            # 1. 减少查询次数
            # 2. 交易记录本身就应该是历史记录，不应该动态改变
            # with db.auto_commit():
            #     drift = Drift()
            #     drift_form.populate_obj(drift)
            #     drift.gift_id = gid
            #     drift.requester_id = current_user.id
            #     drift.requester_nickname = current_user.nickname
            #     drift.gifter_nickname = current_gift.user.nickname
            #     drift.gifter_id = current_gift.user.id
            #     drift.book_title = current_gift.book.title
            #     drift.book_author = current_gift.book.author_str
            #     drift.book_img = current_gift.book.image_large
            #     db.session.add(drift)
            # send_email(current_gift.user.email, '有人想要一本书', 'email/get_gift',
            #            wisher=current_user,
            #            gift=current_gift)
            return redirect(url_for('web.pending'))
    # gift = Gift.query.filter(Gift.id == gid).first_or_404()
    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter,
                           user_beans=current_user.beans, form=drift_form)


@web.route('/pending')
@login_required
def pending():
    drifts = Drift.query.filter(
        or_(Drift.requester_id == current_user.id,
            Drift.gifter_id == current_user.id)).order_by(
        desc(Drift.create_time)).all()
    view_model = DriftViewModel.pending(drifts)
    return render_template('pending.html', drifts=view_model)


@web.route('/drift/<int:did>/reject')
@login_required
def reject_drift(did):
    """
        拒绝请求，只有书籍赠送者才能拒绝请求
        注意需要验证超权
    """
    with db.auto_commit():
        drift = Drift.query.filter(Gift.uid == current_user.id,
                                   Drift.id == did).first_or_404()
        drift.pending = PendingStatus.reject
        # 当收到一个请求时，书籍不会处于锁定状态, 也就是说一个礼物可以收到多个请求
        # gift = Gift.query.filter_by(id=drift.gift_id, status=1).first_or_404()
        # gift.launched = False
    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    """
        撤销请求，只有书籍请求者才可以撤销请求
        注意需要验证超权
    """
    with db.auto_commit():
        # requester_id = current_user.id 这个条件可以防止超权
        # 如果不加入这个条件，那么drift_id可能被修改
        drift = Drift.query.filter_by(
            requester_id=current_user.id, id=did).first_or_404()
        drift.pending = PendingStatus.redraw
        current_user.beans += current_app.config['BEANS_EVERY_DRIFT']
        # gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
        # gift.launched = False
    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    """
        确认邮寄，只有书籍赠送者才可以确认邮寄
        注意需要验证超权
    """
    with db.auto_commit():
        # requester_id = current_user.id 这个条件可以防止超权
        drift = Drift.query.filter_by(
            gifter_id=current_user.id, id=did).first_or_404()
        drift.pending = PendingStatus.success
        current_user.beans += current_app.config['BEANS_EVERY_DRIFT']
        gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
        gift.launched = True
        # 不查询直接更新;这一步可以异步来操作
        Wish.query.filter_by(isbn=drift.isbn, uid=drift.requester_id,
                             launched=False).update({Wish.launched: True})
    return redirect(url_for('web.pending'))
