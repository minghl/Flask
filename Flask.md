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
