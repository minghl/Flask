# views.py: 路由+视图函数
import random

from flask import Blueprint,request, render_template
from sqlalchemy import desc, and_, not_, or_

from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)
@blue.route('/')
def index():
    return 'index'

# 多表操作

# 一对多
# 增加数据
@blue.route('/addgrade/')
def add_grade():
    # 添加班级
    grades = []
    for i in range(10):
        grade = Grade()
        grade.name = f'Jay{i} - {str(random.randint(10, 99))}'
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'

@blue.route('/addstu/')
def add_stu():
    # 添加学生
    students = []
    for i in range(10,20):
        stu = Student()
        stu.name = f'Lucy{i}'
        stu.age = i
        stu.gradeid = random.randint(21,22)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'

# 修改
@blue.route('/updatestu/')
def update_stu():
    stu = Student.query.first()
    stu.age = 100
    db.session.commit()

    return 'OK'

# 删除
@blue.route('/delstu/')
def del_stu():
    # 删除学生
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit()

    return 'OK'

@blue.route('/delgrade/')
def del_grade():
    # 删除班级
    grade = Grade.query.first()
    db.session.delete(grade)
    db.session.commit()

    return 'OK'

# 查询
@blue.route('/getstu/')
def get_stu():
    # 查询某学生所在的班级: 反向引用grade
    stu = Student.query.get(8)
    print(stu.name, stu.age)
    print(stu.gradeid, stu.grade, stu.grade.name, stu.grade.id)

    # 查找某班级下的所有学生
    grade = Grade.query.get(22)
    print(grade.name)
    print(grade.students) # 所有学生
    for stu in grade.students:
        print(stu.name, stu.age)

    return 'OK'