# models.py: 模型，数据库相关

from .exts import db

class User(db.Model):
    # 表名
    __tablename__ = 'tb_user'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(30), unique = True, index = True)
    age = db.Column(db.Integer, default=1)