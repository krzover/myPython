#coding:utf-8
from flask import render_template,request,url_for,redirect
# 根据蓝本设置路由 
from . import auth 
from .. import db 
from ..model import Users 
@auth.route('/login')
def login():

    return render_template('login.html')
@auth.route('/commit_login',methods=['POST'])
def commit_login():
    name = request.form['name']
    psw = request.form['psw']
    user = db.session.query(Users).filter(Users.name==name).first()
    # user 存在且 psw验证成功
    if user and user.verify_psw(psw):

        
        return redirect(url_for('main.index'))
    return 'login failed'

@auth.route('/register')
def register():


    return render_template('register.html')

@auth.route('/commit_register',methods=['POST'])
def commit_register():
    name = request.form['name']
    psw = request.form['psw']
    confirm = request.form['confirm']
    print '>>>>>>>>>',name,psw,confirm
    user = db.session.query(Users).filter(Users.name==name).first()
    print 'user>>>>>>',not user
    # 用户不存在，同时密码一致
    # 判断密码需要匹配字母数字下划线八位
    # 正则表达式（能查出来，赋值给input的pattern属性就可以）
    if not user and psw==confirm:
        current_user = Users(name=name,password=psw)
        db.session.add(current_user)
        db.session.commit()
    # return redirect('/login')
    # 当前蓝本可以加auth，也可以省去；非当前的蓝本，需要加上蓝本名字
    # 这种写法相当于动态加载链接
        return redirect(url_for('.login'))