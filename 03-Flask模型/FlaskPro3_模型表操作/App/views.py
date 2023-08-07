# views.py: 路由+视图函数
from flask import Blueprint
from sqlalchemy import desc, and_, not_, or_

from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user',__name__)
@blue.route('/')
def index():
    return 'index'


# 单表操作
    # 增删改查

# 增：添加数据
@blue.route('/useradd/')
def user_add():
    # 添加一条数据
    # u = User()
    # u.name = 'kun'
    # u.age = 24
    # db.session.add(u) # 将u对象添加到session中
    # db.session.commit() # 同步到数据库中

    # 同时添加多条数据
    users = []
    for i in range(10, 30):
        u = User()
        u.name = '冰冰'+str(i)
        u.age = i
        users.append(u)

    try:
        db.session.add_all(users)
        db.session.commit() # 事务提交
    except Exception as e:
        db.session.rollback() # 回滚
        db.session.flush()
        return 'fail:' + str(e)
    return 'success!'

# 删：删除数据
    # 找到要删除的数据，然后删除
@blue.route('/userdel/')
def user_del():
    u = User.query.first() # 查询第一条数据
    db.session.delete(u)
    db.session.commit()

    return 'success!'


# 改：修改数据
    # 找到要修改的数据，然后修改
@blue.route('/userupdate/')
def user_update():
    u = User.query.first()  # 查询第一条数据
    u.age = 1000
    db.session.commit()

    return 'success!'

# 查：查询数据
#   条件
@blue.route('/userget/')
def user_get():
    # all(): 返回所有数据，返回列表
    users = User.query.all()
    # print(users)
    # print(users, type(users)) # <class 'list'>
    # print(User.query, type(User.query)) # <class 'flask_sqlalchemy.query.Query'>

    # filter(): 过滤，得到查询集，类似SQL中的where
    users = User.query.filter().filter() # 可以继续操作
    # print(users, type(users)) # 查询集
    # print(list(users)) # 强制转换列表

    # get(): 查询到对应主键的数据对象
    user = User.query.get(8)
    # print(user, type(user)) # <class 'App.models.User'>
    # print(user.name, user.age) # 获取数据的属性

    # filter(): 类似SQL中的where
    # filter_by(): 用于等值操作的过滤
    # users = User.query.filter(User.age==20)
    # users = User.query.filter_by(age = 20)
    users = User.query.filter(User.age>20) # 可以用于非等值操作
    # print(list(users))

    # first(): 第一条数据
    # first_or_404(): 第一条数据，如果不存在则抛出404错误
    user = User.query.first()
    # user = User.query.filter_by(age=100).first_or_404()
    # print(user)

    # count(): 统计查询集中的数据条数
    users = User.query.filter()
    # print(users.count()) # 20

    # limit(): 前几条
    # offset(): 跳过前几条
    users = User.query.offset(3).limit(4)
    # print(list(users))

    # order_by(): 排序
    users = User.query.order_by('age') # 升序
    users = User.query.order_by(desc('age')) # 降序
    # print(list(users))

    # 逻辑运算: and_,or_,not_
    users = User.query.filter(User.age>20, User.age<25) # 且，常用
    users = User.query.filter(and_(User.age>20, User.age<25)) # 且
    users = User.query.filter(or_(User.age>25, User.age<20)) # 或
    users = User.query.filter(not_(or_(User.age>25, User.age<20))) # 非
    # print(list(users))

    # 查询属性
    # contains('3'): 模糊查找，类似SQL中的like
    users = User.query.filter(User.name.contains('3'))
    # in_(): 其中之一
    users = User.query.filter(User.age.in_([10,20,30,40,50]))
    # startswith(): 以某子串开头
    # endswith(): 以某子串结尾
    users = User.query.filter(User.name.startswith('冰'))
    users = User.query.filter(User.name.endswith('2'))

    # __gt__: 大于
    users = User.query.filter(User.age.__gt__(25))


    print(list(users))

    return 'success'