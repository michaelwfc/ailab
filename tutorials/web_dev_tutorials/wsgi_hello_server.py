"""
@author: michaelwfc
https://www.liaoxuefeng.com/wiki/1016959663602400/1017805733037760

@version: 1.0.0
@license: Apache Licence
@file: hello_wsgi.py
@time: 2023/9/4 23:48
"""

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server


# 导入我们自己编写的application函数:
def application(environ, start_response):
    # 发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。
    # start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器
    # return [b'<h1>Hello, web!</h1>']
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 127.0.0.1:8000 ...')
# 开始监听HTTP请求:
httpd.serve_forever()