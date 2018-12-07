"""
    Created by 朝南而行 2018/12/7 14:01
"""

# 测试代码

from flask import Flask, current_app

app = Flask(__name__)
# 应用上下文 对象 对Flask的封装
# 请求上下文 对象 对Request的封装
d = current_app.config['DEBUG']
