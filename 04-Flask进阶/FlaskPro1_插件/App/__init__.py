# __init__.py: 初始化文件，创建Flask应用

from flask import Flask
from .views import blue
from .exts import init_exts

import os
# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # /Users/liminghao/Documents/Study/Flask/04-Flask进阶/FlaskPro1_插件
print('BASE_DIR:',BASE_DIR)
# BASE_DIR: flast插件，项目目录

def create_app():
    # 配置静态文件和模版文件目录
    # static_folder = '../static'
    # template_folder = '../templates'

    static_folder = os.path.join(BASE_DIR, 'static')
    template_folder = os.path.join(BASE_DIR, 'templates')
    app = Flask(__name__, static_folder=static_folder,template_folder=template_folder)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    db_uri = 'sqlite:///sqlite3.db'
    # db_uri = 'mysql+pymysql://root:@localhost:3306/flaskdb' # mysql 的配置·
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri  # 配置连接数据库路径DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改

    # 初始化插件
    init_exts(app = app)

    return app