# views.py: 路由+视图函数
from flask import Blueprint,request,render_template
from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('book',__name__)
@blue.route('/')
@blue.route('/bookindex/')
def book_index():
    return render_template('book_index.html')

@blue.route('/booklist/')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html',books=books)

@blue.route('/bookdetail/<int:bid>/')
def book_detail(bid):
    book = Book.query.get(bid)
    return render_template('book_detail.html', book=book)

# 作者详情
@blue.route('/authordetail/<int:aid>/')
def author_detail(aid):
    author = Author.query.get(aid)
    return render_template('author_detail.html', author=author)

# 出版社详情
@blue.route('/publisherdetail/<int:pid>/')
def publisher_detail(pid):
    publisher = Publisher.query.get(pid)
    return render_template('publisher_detail.html', publisher=publisher)
