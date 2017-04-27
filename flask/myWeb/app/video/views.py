#coding:utf-8

from . import video 
from flask import render_template,redirect,url_for,request,url_for
from ..model import Teachers,Users,Kind,Videos,Courses
from .. import db
import datetime

@video.route('/video_manage/<id>')
def manage(id):
    video  = db.session.query(Videos).filter(Videos.c_id==id).all()
    return  render_template('video/video.html',data=video,id=id)


@video.route('/addvideo/<id>')
def addvideo(id):
    tea = db.session.query(Teachers).all()
    return render_template('video/addvideo.html',data=tea,id=id)


@video.route('/commit_add/<id>',methods=['post'])
def commit_add(id):
    title=request.form['title']
    time=int(request.form['time'])
    hits=int(request.form['hits'])
    abstract=request.form['abstract']
    t_id=int(request.form['teacherlabel'])

    addtime = datetime.datetime.now()

    c_id =int(id)
    vid = Videos(title=title,time=time,hits=hits,abstract=abstract,t_id=t_id,addtime=addtime,c_id=c_id)
    db.session.add(vid)
    db.session.commit()
    return render_template('video/video.html/')


@video.route('/deletevideo',methods=['post'])
def deletevideo():
    id = request.form['id']
    video = db.session.query(Videos).filter(Videos.id==id).first()
    db.session.delete(video)
    db.session.commit()
    return 'success'

