#coding:utf-8

from . import auth
from flask import render_template,redirect,url_for,request,session
from .. import db
from ..model import Users

@auth.route('/register')
def index():

    return render_template('register.html')

@auth.route('/')
def mian_view():
    return render_template('base.html')

@auth.route('/index')
@auth.route('/login')
def  login():
    return render_template('login.html')


@auth.route('/commit_reg' ,methods=['post'])
def com_reg():
    name = request.form['name']
    psw = request.form['psw']
    repsw = request.form['repsw']
    user = db.session.query(Users).filter(Users.user_id==name).first()

    if psw==repsw and not user:
        user = Users(user_id=name,password=psw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
    else:
        return render_template('error.html')
    

@auth.route('/commit_login',methods=['post'])
def com_login():
    name = request.form['name']
    psw = request.form['psw']
    user = db.session.query(Users).filter(Users.user_id==name).first()
    if user and user.check_psw(psw):    
        session['islogin']=True
        return redirect(url_for('.mian_view'))
    else:
        return render_template('error.html')

@auth.route('/logout')
def logout():
    session['islogin'] = False

    return redirect(url_for('.login'))