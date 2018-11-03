
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

# 发送邮件功能：
#   1 能够群发多条邮件，每隔3秒进行发送

# 第三方 SMTP 服务
mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "15907813604@163.com"                  # 用户名
mail_pass = "xiaoe520"               # 授权密码，非登录密码

sender = '15907813604@163.com'    # 发件人邮箱(最好写全, 不然会失败)
receivers = '1741847070@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


title = 'api官网上线啦'  # 邮件主题
content = '我正在用Python给您发邮件，来看看吧'  # 邮件内容


def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败：' + str(e))


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


if __name__ == '__main__':
    a = 1
    while a > 0:
        sendEmail()
        a -= 1
