# views.py: 路由+视图函数
from flask import Blueprint, render_template, jsonify, request
from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)
@blue.route('/')
def index():
    return 'index'

# 前后端不分离:
#   render_template('.html', users=users)

# 前后端分离:
#   后端返回json字符串：jsonify()
#   前端使用ajax来请求数据：ajax

# jsonify(): 序列化

# HTTP请求方式：
#   GET：获取数据
#   POST：新增数据
#   PUT：修改数据
#   DELETE：删除数据

@blue.route('/users/', methods=['GET','POST','PUT','DELETE'])
def users():
    if request.method == 'GET':
        return jsonify({'method':'GET'})
    elif request.method == 'POST':
        return jsonify({'method':'POST'})
    elif request.method == 'PUT':
        return jsonify({'method':'PUT'})
    elif request.method == 'DELETE':
        return jsonify({'method':'DELETE'})