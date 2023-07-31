# models.py: 模型，数据库相关

from .exts import db

# 模型 -> 数据库
#  类 -> 表结构
# 类属性 -> 表字段
# 对象 -> 表的一行数据

# 模型Model：类
# 必须继承db.Model
# 改模型，直接改这里
# 模型一旦改掉，就需要重新迁移
class User(db.Model):
    # 表名
    __tablename__ = 'tb_user'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(30), unique = True, index = True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    salary = db.Column(db.Float, default=100000, nullable=False)
    salary2 = db.Column(db.Float, default=100000, nullable=False)
# db.Column: 表示字段
# db.Integer: 表示整数
# primary_key = True: 主键
# autoincrement=True: 自动递增
# db.String(30): varchar(30) 可变字符串
# unique = True: 唯一约束
# index = True: 普通索引
# default=100000: 默认值
# nullable=False: 是否允许为null