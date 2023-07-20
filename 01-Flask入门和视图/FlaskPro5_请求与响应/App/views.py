# views.py: 路由+视图函数
from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for
from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)
@blue.route('/')
def index():
    return 'index'

# 请求和响应
# request：请求
# response：响应

# http一次前后端交互：先请求，后响应

# Request: 客户端向服务器端发送的请求
@blue.route('/request/',methods=['GET','POST'])
def get_request():
    pass
    # print(request) # <Request 'http://127.0.0.1:5000/request/' [GET]>

    # 重要属性
    print(request.method) # 请求方式，GET或者POST...

    # GET请求参数
    # ImmutableMultiDict: 类字典对象，区别是可以出现重复的key
    print(request.args)
    # print(request.args['name'])
    # print(request.args.get('name')) # 用得最多，避免报错
    # print(request.args.getlist('name'))

    # POST请求的参数
    print(request.form)
    # print(request.form.get('name')) #lucy

    # cookie
    print(request.cookies) # ImmutableMultiDict([('name', 'hello')])

    # 路径
    print(request.path) # /request/
    print(request.url) # http://127.0.0.1:5000/request/?name=lisi&age=33
    print(request.base_url) # http://127.0.0.1:5000/request/
    print(request.host_url) # http://127.0.0.1:5000/
    print(request.remote_addr) # 127.0.0.1 客户端的ip

    print(request.files) # 文件内容，ImmutableMultiDict([])
    print(request.headers) # 请求头

    print(request.user_agent) # 用户代理，包括浏览器和操作系统的信息，python-requests/2.31.0

    return 'request ok!'

# Response: 服务器端想客户端发送的响应
@blue.route('/response/')
def get_response():
    pass
    # 响应的几种方式
    # 1. 返回字符串（不常用）
    # return 'response OK!'

    # 2. 模版渲染（前后端不分离）
    # return  render_template('index.html', name='张三', age=33)

    # 3. 返回json数据（前后端分离）
    data = {'name':'李四','age':44}
    # return data

    # jsonify()：序列化，字典=>字符串
    # return jsonify(data)

    # 4. 自定义Response对象
    html = render_template('index.html', name='张三', age=33)
    print(html, type(html)) #<class 'str'>

    # res = make_response(html, 200)
    res = Response(html)
    return res

# Redirect: 重定向
@blue.route('/redirect/')
def make_redirect():
    pass
    # 重定向的几种方式
    # return redirect('https://www.qq.com')
    # return redirect('/response/')

    # url_for():反向解析，通过视图函数名反过来找到路由
    # url_for('蓝图名称.视图函数名')
    # ret = url_for('user.get_response')
    # print('ret:',ret)
    # return redirect(ret)

    # url_for传参
    ret2 = url_for('user.get_request',name='王五',age=66)
    return redirect(ret2)

