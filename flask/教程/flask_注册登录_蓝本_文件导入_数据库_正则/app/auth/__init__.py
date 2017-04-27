#coding:utf-8
#创建蓝本
from flask import Blueprint 

auth = Blueprint('auth',__name__)
# 导入路由  ，这个位置是防止交叉倒入错误
from . import views