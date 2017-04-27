#coding:utf-8
from flask import render_template,redirect,url_for,request,session
from .. import db
from ..model import Users
# 根据蓝本设置路由 
from . import auth




@auth.route('/login')
def login():
    data = {'islogin':session.get('islogin')}
    return render_template('login.html',data=data)

@auth.route('/commit_login',methods=['POST'])

def commit_login():
    name = request.form['name']
    psw = request.form['psw']
    user = db.session.query(Users).filter(Users.name==name).first()
    if user and user.verify_psw(psw):
        session['islogin'] = True

        return redirect(url_for('.index'))


@auth.route('/register')
def register():
    data = {'islogin':session.get('islogin')}
    return render_template('register.html',data=data)


@auth.route('/commit_r',methods=['POST'])
def commit():
    name = request.form['name']
    psw = request.form['psw']
    confirm = request.form['confirm']
    if psw==confirm:
        
        user = Users(name=name,psw=psw)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

@auth.route('/commit_register',methods=['POST'])
def commit_register():
    name = request.form['name']
    psw = request.form['psw']
    confirm = request.form['confirm']
    
    if not db.session.query(Users).filter(Users.name==name).first() and psw==confirm:
        user = Users(name=name,psw=psw)
        db.session.add(user)
        db.session.commit()

    return redirect(url_for('.login'))



@auth.route('/logout')
def logout():
    session['islogin'] = False
    return redirect(url_for('.index'))

@auth.route('/index')
def index():
    data = {'islogin':session.get('islogin')}
    return render_template('index.html',data=data)