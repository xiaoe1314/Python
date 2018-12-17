"""
    Created by 朝南而行 2018/12/5 16:36
"""

# True会执行两次 restart
# False只执行一次
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
# 下面两段代码解决这个问题 https://blog.csdn.net/gbz2000/article/details/79506110
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
# 随机字符串，保证唯一
SECRET_KEY = '\x88D\xf09\x84\x07\x11\xd23\xa45\xec85D\x14\x8f\xf58\x68c'








