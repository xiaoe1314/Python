import smtplib
import textwrap
import time
from email.header import Header
from email.mime.text import MIMEText

# 发送邮件功能：
#   1 能够群发多条邮件，每隔5秒进行发送
#   2 能够群发多条邮件，每隔3秒进行发送


class SendEmail:
    def __init__(self):
        # 第三方 SMTP 服务
        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "xiaoheixianbao@163.com"  # 用户名
        mail_pass = "zz123456"  # 授权密码，非登录密码

        sender = 'xiaoheixianbao@163.com'  # 发件人邮箱(最好写全, 不然会失败)

        title = 'xiaoheixianbao@163.com'  # 邮件主题
        content = 'xiaoheixianbao@163.com'  # 邮件内容
        with open('a.txt', 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                # 全掉前后的空格
                account = line.strip() + '@qq.com'
                self.parse_start(account, title, content, sender, mail_host, mail_user, mail_pass)
                time.sleep(3)

    # account接收邮件，可设置为你的QQ邮箱或者其他邮箱
    def parse_start(self, account, title, content, sender, mail_host, mail_user, mail_pass):
        print(account)
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(account)
        message['Subject'] = title

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            smtpObj.sendmail(sender, account, message.as_string())  # 发送
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败：' + str(e))


if __name__ == '__main__':
    SendEmail()
