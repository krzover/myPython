#coding:utf-8

from . import main
from flask import render_template,redirect,url_for,request
from ..model import Teachers,Users,Kind,Videos,Courses
from .. import db
import datetime


@main.route('/teachermaster')
def index():
    name = db.session.query(Teachers.name).all()
    abstract = db.session.query(Teachers.abstract).all()
    level = db.session.query(Teachers.level).all()
    data = zip(name,abstract,level)
    return render_template('teachermaster.html',data=data)


@main.route('/classmaster')
def classmaster():
    name = db.session.query(Kind).all()

    return redirect(url_for('.rename',name=name[0].name))

@main.route('/<name>')
def rename(name):
    all_kinds = db.session.query(Kind).all()
    na = db.session.query(Kind).filter(Kind.name==name).first()
    kid = na.id
    course = na.course
    data = {'name':name,'courses':course,'kinds':all_kinds,'kid':kid}
    return render_template('classmaster.html',data=data)

@main.route('/commit_delete_course',methods=['post'])
def del_course():
    id = request.form['id']
    course = db.session.query(Courses).filter(Courses.id==id).first()
    db.session.delete(course)
    db.session.commit()
    return 'success'

@main.route('/commit_change_course',methods=['post'])
def change_course():
    aid = request.form['id']
    course = db.session.query(Courses).filter(Courses.id==aid).first()
    course.title = request.form['name']
    course.abstract = request.form['abs']
    # courses.addtime = addtime
    print '<><>',course,'<><>',course.title,'<><>',course.abstract
    db.session.commit()
    return 'success'

@main.route('/commit_addcourse',methods=['post'])
def addcourse():
    title = request.form['c_title']
    abst = request.form['c_abst']
    k_id = request.form['k_id']
    time = datetime.datetime.now()
    cour = Courses(title=title,abstract=abst,addtime=time,k_id=k_id)
    db.session.add(cour)
    db.session.commit()
    return 'success'