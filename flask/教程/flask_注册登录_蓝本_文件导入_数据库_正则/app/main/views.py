#coding:utf-8
# 根据蓝本设置路由
from . import main
from flask import render_template,redirect,url_for,request
# 装饰器 不是app.route,变成了main
@main.route('/index')
def index():

    return render_template('index.html')