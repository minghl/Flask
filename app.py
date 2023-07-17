from flask import Flask

# __name__ 表示当前模块，app.py，项目目录
# 创建flask应用对象
app = Flask(__name__)

# 前端返回路径
# 进入下面视图函数
# 路由route+视图函数hello_world
@app.route('/')
def hello_world():  # put application's code here
    # 响应一定要有返回值，视图函数不然会报错
    # 响应：返回给浏览器的数据
    return 'Hello World!'

# 添加一个路由和视图函数
@app.route('/index/')
def index():
    return 'Index 首页'

if __name__ == '__main__':
    # 最后运行
    # 启动服务器
    app.run()
