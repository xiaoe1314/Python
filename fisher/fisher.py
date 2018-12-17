"""
    Created by 朝南而行 2018/12/5 16:36
"""
from app import create_app


app = create_app()


# 装饰器注册url (视图函数)
#@app.route('/hello')
#def hello():
    # 基于类的视图 （即差视图）
    # 会返回：status code 200 404 301
    # content-type -> http headers
    # 如果不指定content-type类型，默认是
    # content-type = text/html
    # 永远返回Response对象
    # 状态码不会影响你返回的内容
    # 如果是写接口（api）的话，字符串要是json格式的字符串
    # 而且content-type = application/json
    # headers = {
    #     'content-type': 'text/plain',
    #     'location': 'https://www.jianshu.com/'
    # }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return '<html></html>', 301, headers


# 普通函数
# 视图和普通函数的区别，视图函数做了很多的封装
# def hello0():
    # 基于类的视图 （即差视图）
    # return 'Hello World!'


# 有一种方式是需要url这种方式注册url
# app.add_url_rule('/hello', view_func=hello)




# if __name__ == '__main__'的作用是什么呢
# 在入口文件增加了这样的判断，if里面的语句只在入口文件执行
# 如果这个文件不是作为入口文件被执行的，而是被其他模块导入执行的，那么这个if里面的语句是不会被执行的

# 问题：在我们flask项目中的入口文件增加这样的if判断，然后在启动web服务器这样对我们有什么意义
# 回答：我们在开发过程中使用的是调试模式，而使用的是flask 自带的服务器，当我们需要部署项目到
# 生产环境中的时候是不需要使用flask 自带的服务器，而是使用Nginx + uwsgi 来形式进行部署
# Nginx 作为前置服务器用于接收我们浏览器发送过来的请求，接着会转发这个请求给uwspi ,生产环境下
# flask项目的启动并不像我们直接run,或者python + 入口文件执行的，而是uwsgi加载我们入口文件的模块
# 来启动相关的代码，这样入口文件就不在是启动文件了，而是生产环境加载的一个模块，app.run 是不会被执行的
# 那么如果没有这个if 判断的话，就会启动了flask 自带的服务器
if __name__ == '__main__':
    # 调试模式（性能差，不能展示错误信息给用户） flask 自带的服务器
    # 生产环境 Nginx + uwsgi （一般是不会使用flask自带的服务器）
    app.run(host='0.0.0.0', port='1009', debug=app.config['DEBUG'])
    # app.run(debug=True)
