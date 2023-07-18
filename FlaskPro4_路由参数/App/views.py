# views.py: 路由+视图函数
from flask import Blueprint
from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'

# 路由参数
    # string接收任何没有斜杠（'/'）的字符串（默认）
    # Ent接收整型
    # float接收浮点型
    # path接收路径，可接收斜线
    # uuid只校受4uid宁符串，唯一码，一种生成规则
    # any可以同时指定多种路径，进行限定

# string: 重点
@blue.route('/string/<string:name>/')
def get_string(name):
    print(type(name))
    return name

# int
@blue.route('/int/<int:id>/')
def get_int(id):
    print(type(id)) # <class 'int'>
    return str(id)

# float
@blue.route('/float/<float:money>/')
def get_float(money):
    print(type(money)) # <class 'float'>
    return str(money)

# path: 支持/的字符串
@blue.route('/path/<path:name>/')
def get_path(name):
    print(type(name)) # <class 'str'>
    return str(name)

# uuid: 5a98bd4d-060b-4fb1-9e07-cbb800a3c8c6
@blue.route('/uuid/<uuid:id>/')
def get_uuid(id):
    print(type(id)) # <class 'uuid.UUID'>
    return str(id)

@blue.route('/getuuid/')
def get_uuid2():
    import uuid
    return str(uuid.uuid4())

# any: 从列出的项目中选择一个
@blue.route('/any/<any(apple, orange, banana):fruit>/')
def get_any(fruit):
    print(type(fruit)) # <class 'str'>
    return str(fruit)

# methods: 请求方式
# 默认不支持POST
# 如果需要同时支持GET和POST，就设置methods
@blue.route('/methods/', methods=['GET','POST'])
def get_methods():
    return 'methods'