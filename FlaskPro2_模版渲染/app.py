from flask import Flask, render_template, jsonify

app = Flask(__name__)

#路由
@app.route('/')
def home():
    # 返回字符串
    return 'Flask Home2'

# 渲染模版
@app.route('/index/')
def index():
#     返回字符串:支持html标签
#     return '<b>Flask Index</b>'

# 模版渲染
    return render_template('index.html', name='法外狂徒张三')

# JSON
# jsonify: 序列化,转成字符串
#     return jsonify({'name':'张三','age':33})
if __name__ == '__main__':
    # 防止一直重启，启动
    app.run(debug=True)

    # run(）启动所时候还可以添加参数：
    # debug是否开启调试模式，开启后修改过python代码会自动重启
    # port启动指定服务器的诺口号，默认是5000
    # host主机，默认是127.0.0.1，指定为0.0.0.0代表本机所有ip