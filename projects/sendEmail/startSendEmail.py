
import smtplib
import time
from email.mime.text import MIMEText

# 发送邮件功能：
#   1 能够群发多条邮件，每隔3秒进行发送


class send(object):
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "xiaoheixianbao@163.com"  # 用户名
    mail_pass = "zz123456"  # 授权密码，非登录密码
    sender = 'xiaoheixianbao@163.com'  # 发件人邮箱(最好写全, 不然会失败)

    title = '淘宝购物优惠卷加返利   https://upload-images.jianshu.io/upload_images/1150982-6bbb50581e72e6ae.jpg'  # 邮件主题
    # 邮件内容
    content = '666'
    # content = """
    # <html>
    #     <body>
    #         <div class="qmbox" style="width:100%;">
    #             <p class="MsoNormal" align="left">
    #                 <span style="font-size: 12pt; font-family: 宋体;">淘宝购物优惠卷加返利</span>
    #                 <a href="https://upload-images.jianshu.io/upload_images/1150982-6bbb50581e72e6ae.jpg" rel="noopener" target="_blank">
    #                     https://upload-images.jianshu.io/upload_images/1150982-6bbb50581e72e6ae.jpg
    #                 </a>
    #             </p>
    #         </div>
    #     </body>
    # </html>
    # """

    def __init__(self):
        with open('a.txt', 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                # 全掉前后的空格
                account = line.strip() + '@qq.com'
                self.sendContent(account)
                time.sleep(10)

    def sendContent(self, account):
        # message = MIMEText(self.content, 'plain', 'utf-8')  # 内容, 文本格式, 编码
        message = MIMEText(self.content, 'html', 'utf-8')  # 内容, html格式, 编码
        message['From'] = "{}".format(self.sender)
        message['To'] = ",".join(account)
        message['Subject'] = self.title


        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
            smtpObj.sendmail(self.sender, account, message.as_string())  # 发送
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败：' + str(e))


if __name__ == '__main__':
    send()

