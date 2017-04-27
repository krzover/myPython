#coding:utf-8
# 创建蓝本

from flask import Blueprint 
# 创建蓝本，第一个参数 就是当前文件夹名字，第二个用__name__
course = Blueprint('course',__name__)

# 写下边是为了防止交叉倒入错误
from . import views

