from flask import jsonify
from flask_restful import Resource

# 类视图：CBV Class Based View
# 视图函数：FBV Function Based View
class HelloResource(Resource):
    def get(self):
        return jsonify({'msg':'get请求'})

    def post(self):
        return jsonify({'msg':'post请求'})