# models.py: 模型，数据库相关

from .exts import db

# 多表关系
# 一对多
# 班级:学生 = 1:N
# 班级表
class Grade(db.Model):
    # 表名
    __tablename__ = 'grade' # 表名
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(30), unique = True)
    # 建立关联
    #   第1个参数：关联的模型名（表）
    #   第2个参数：反向引用的名称，grade对象，
    #            让student去反过来得到grade对象的名称
    #   第3个参数：懒加载
    #   这里的students不是字段，是类属性
    students = db.relationship('Student', backref='grade', lazy=True)

# 学生表
class Student(db.Model):
    # 表名
    __tablename__ = 'student' # 表名
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(30), unique = True)
    age = db.Column(db.Integer)
    # 外键: 跟Grade表中的id字段关联
    gradeid = db.Column(db.Integer, db.ForeignKey(Grade.id))