# views.py: 路由+视图函数
from flask import Blueprint
from .models import *
from .exts import cache
import time

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)

# 使用缓存
@blue.route('/')
@cache.cached(timeout=20) # 给视图函数加一个缓存20秒（20秒之后才会重新sleep5秒）
def index():
    print('Index2')

    time.sleep(5)
    return 'index'