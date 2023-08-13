# Flask

## 01 Flask 入门和视图

- Python后端的2个主流框架
  - Flask 轻量级框架
  - Django 重型框架
- Flask 是一个基于MVC设计模式的web后端框架
  - MVC：
    - M Model 数据模型
    - V View 界面
    - C Controller 控制器
  - MTV：类似MVC
    - M Models 模型（数据）
    - T Templates 模版（界面）
    - V Views 视图（控制器）
- Flask依赖三个库：
  - Jinja2 模版引擎{% %} 
  - 模版：静态html+模版语言{% %}
  - Werkzeug：WSGI 工具集
- Flask流行的原因：
  - 有非常齐全的官方文档，好上手
  - 有非常好的扩展机制和第三方扩展环境，工作中常见的软件都会有对应的扩展。自己动手实现扩展也很容易
  - 社区活跃度非常高
  - 微型框架的形式给了开发者更大的选择空间

## 02 Flask框架流程图和MVT模式

![Screenshot 2023-06-27 at 16.30.09](/Users/liminghao/Library/Application Support/typora-user-images/Screenshot 2023-06-27 at 16.30.09.png)

## 03 virtual env 虚拟环境

https://phoenixnap.com/kb/install-flask

## 04 会话技术

http协议：

1. 先请求，后响应
2. 响应后会断开连接
3. 一次请求就结束了

Cookie:
	作用：让服务器能够认识浏览器，常用于登录

1. 登录
2. 验证用户名和密码，设置好cookie（和登录用户绑定），返回给浏览器
3. 浏览器会自动存储cookie到本地
4. 下一次在请求，会自动携带浏览器的cookie
5. 取出cookie的值，判断是哪个用户在访问，返回对应用户的数据
6. 用户数据

Cookie特点：

- 客户端会话技术，浏览器的会话技术
- 数据全都是存储在客户端中
- 存储使用的键值对结构进行的存储
- 特性
  - 支持过期时间
  - 默认会自动携带本网站的所有cookie
  - 根据域名进行cookie存储
  - 不能跨域名
  - 不能跨浏览器
- Cookie是通过服务器创建的Response来创建的

设置cookie:

```python
response.set_cookie(key, value[,max_age=None, exprise=None])
	max_age: 整数，指定cookie过期时间
  expries: 整数，指定过期时间，可以制定一个具体日期时间
  max_age和expries两个选一个指定
```

获取cookie:

```python
request.cookie.get(key)
```

删除cookie

```python
response.delete_cookie(key)
```

Session:
	服务端会话技术，依赖于cookie

- 服务端的会话技术
- 所有数据存储在服务器中
- 默认存储在内存中
- 存储结构也是key-value形势，键值对
- session是离不开cookie的

Flask中的session是全局对象（之前的request也是Flask的一个全局对象）

常用操作：
	设置sesiion

```python
session['key'] = value
```

​	获取session

```python
session.get(key,default=None)根据键获取会话的值
```

​	删除session

```python
session.pop(key) 删除某一值
session.clear()	清除所有
```

Cookie和Session的区别：

Cookie:

1. 在浏览器存储
2. 安全性较低
3. 可以减轻服务器压力

Session:

1. 在服务器端存储
2. 安全性高
3. 对服务器要求较高
4. 依赖cookie

## 05 模版Template

模版是呈现给用户的界面

在MVT中充当T的角色，实现了MT的解耦，开发中VT有着N：M的关系，一个V可以调用任意T，一个T可以被任意V调用
模版处理氛围两个过程

1. 加载HTML
2. 模版渲染（模版语言）

模版代码包含两个部分

1. 静态HTML
2. 动态插入的代码段（模版语法）

### Jinja2

Flask中使用Jinja2模版引擎

Jinja2由Flask作者开发
	一个现代化设计和友好的Python模版语言
	模仿Django的模版引擎

优点
	速度快，被广泛使用
	HTML设计和后端Python分离
	减少Python复杂度
	非常灵活，快速和安全
	提供了控制，继承等高级功能

### 模版语法

模板语法主要分为两种
	变量
	标签

模板中的变量{{var }}
	视图传递给模柀的数据
	前面定义出来的数据
	变量不存在，默认忽略

模板中的标签{% tag %}
	控制逻辑
	使用外部表达式
	创建变量
	宏定义

### 结构标签

block 块操作
	父模板挖坑，子模板填坑
	{% block xxx %}
	{% endblock %}

extends 継承
	{% extends '×××' %}
	继承后保留块中的内容
	{{super() }}

include
	包含，将其他html包含进来，
	{% include 'xxx' %}

marco【了解】
	宏定义，可以在模板中定义西数，在其它地方调用
	{% macro hello(name) %}
		{{ name }}
	{% endmacro %}

宏定义可导入
	{% from 'xxx' import xxx %}

### 循环

## 06 Model

### 01 数据迁移

1. 安装好数据迁移的包 flask-sqlalchemy和flask-migrate

2. 在exts.py中初始化Migrate和SQLAlchemy

3. 在models中定义好模型

4. 在views.py中一定要导入models模块

   from .models import *

5. 配置好数据库（sqlite3或MySQL）

6. 执行数据迁移命令：

   1. 先在cmd或Terminal进入项目目录（app.py所在目录）：

   2. 然后输入命令：

      flask db init 创建迁移文件夹migrates，只调用一次

      flask db migrate 生成迁移文件

      flask db upgrade 执行迁移文件中的升级

      flask db downgrade 执行迁移文件中的降级

数据筒単操作
	创建数据库，表
		db.create_al1()
	删除表
		db.drop_all()
	在事务中外理，数据插入
		db.session.add(object)
		db.session.commit ()
	获取所有数据
		Person. query. all ()

### 02 模型操作

#### 创建模型

```python
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
```

##### 字段类型

<img src="/Users/liminghao/Library/Application Support/typora-user-images/Screenshot 2023-07-31 at 13.00.35.png" alt="Screenshot 2023-07-31 at 13.00.35" style="zoom:33%;float:left;"/>

##### 常用约束

![Screenshot 2023-07-31 at 13.03.37](/Users/liminghao/Library/Application Support/typora-user-images/Screenshot 2023-07-31 at 13.03.37.png)

#### 模型操作

##### 单表操作

查询数据
	过滤器
		filter () 把过滤器添加到原查询上，返回一个新查询
		filter_by(）把等值过滤器添加到原查询上，返回一个新查询
		limit () 使用指定的值限制原查询返回的结果数量，返回一个新查询
		offset ()  偏移原查询返回的结果，返回一个新查询
		order_by(）根据指定条件对原查询结果进行排序，返回一个新查询
		grouP_by(）根据指定条件对原查询结果进行分组，返回一个新查询

​	常用查询
​		all () 以列表形式返回查询的所有结果，返回列表
​		first(）返回查询的第一个结果，如果没有结果，则返回None
​		first_or_404（）返回查询的第一个结果，如果没有结果，则终止请求,返回404错误响应
​		get(）返回指定主键对应的行，如果没有对应的行，则返回None
​		get_or_404() 返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回404错误响应
​		count（）返回查询结果的数量
​		paginate(）返回一个paginate对象，它包含指定范国内的结果

查询属性
	contains
	startswith
	endswith
	in_
	\_\_gt_\_
	\_\_ge\_\_
	\_\_lt\_\_	
	\_\_le\_\_		

逻辑运算
	与 and_
		filter(and_(条件),条件...)
	或 or\_
		filter(or\_条件,条件...)
	非 not\_
		filter(not\_(条件),条件...)

##### 分页

- 手动做分页

  Persons = Person.query.offset((page - 1) * per_page).limit(per_page)

- 使用paginate做分页

  persons = Person.query.paginate(page = page, per_page = per_page, error_out = False).items

##### 多表操作

- 多表关系
  - 一对一   1:1   用户表:身份证表   1个用户只有一张身份证   1张身份证只对应一个用户
  - 一对多   1:N   班级表:学生表   1个班级有多个学生   1个学生只属于一个班级 
  - 多对多   N:M   用户表:收藏表:电影表   1个用户可以收藏多部电影   一部电影可以被多个用户收藏  （会用到中间表）
    用户表:中间表   1:N   电影表:中间表   1:N

## 07 Flask进阶

### Flask插件

#### Flask-caching

给视图函数加一个缓存20秒（20秒之后才会重新sleep5秒）

#### 钩子（中间件middleware）

钩子或者钩子函数，是指在执行函数和目标函数之间挂载的函数，框架开发者给调用方提供一个point-挂载点，是一种AOP切面编程思想

常用的钩子函数：
	before_first_request: 处理第一次请求之前执行
	before_request: 在每次请求之前执行，通常使用这个钩子函数预处理一些变量，实现反爬等
	after_request: 注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行
	teardown_appcontext: 当APP上下文被移除之后执行的函数，可以进行数据库的提交或者回滚	
