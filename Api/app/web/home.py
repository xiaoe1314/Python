"""
    Created by 朝南而行 2018/12/26 11:18
"""
from flask import render_template, request, flash

from app.form.custom import CustomURL
from app.web import web
import json


@web.route('/')
def home():
    # video_url = request.args['url']
    # video_url = request.args.get("url")
    # if video_url:
    #     return render_template('index.html', url=video_url)
    return render_template('index.html')


@web.route('/custom/api')
def custom():
    return render_template('custom.html')


    # a = {
    #     'msg': request.headers.items(),
    #     456: '123',
    #     789: '123',
    #     159: '123'
    # }
    # return json.dumps(a, default=lambda o: o.__dict__, ensure_ascii=False), 200, {'content-type': 'application/json'}
