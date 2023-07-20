# views.py: 路由+视图函数
from flask import Blueprint, render_template
from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)
@blue.route('/')
def home():
    pass

    data  = {
        'name':'ikun ikun ikun',
        'age':26,
        'likes':['ball','sing','dance','code']
    }
    # return render_template('home.html', **data)

    return  render_template('child2.html', **data)
