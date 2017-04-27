#coding:utf-8
from flask import render_template
# 根据蓝本设置路由 
from . import auth 
@auth.route('/login')
def login():

    return render_template('login.html')

