# models.py: 模型，数据库相关

from .exts import db

# 类 => 表
# 类属性 => 表字段
# 对象 => 表的一条数据

class User(db.Model):
    # 表名
    __tablename__ = 'user'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(30), unique = True)
    age = db.Column(db.Integer, default=1)

    def __repr__(self):
        return self.name