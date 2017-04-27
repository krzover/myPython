#coding:utf-8
from . import video 

from flask import render_template,redirect,url_for,request ,session
from .. import db 
from ..model import Videos,Teachers
import datetime
# 视频列表
@video.route('/myvideo/<id>')
def myvideo(id):
    videos = db.session.query(Videos).filter(Videos.c_id==id).all()
    # 获取教师名字
    name = []
    for item in videos:
        teacher = db.session.query(Teachers).filter(Teachers.id==item.t_id).first()
        name.append(teacher.name)
    print '>>>>>>>>>',videos
    data = {'islogin':session.get('islogin'),'videos':videos,'name':name,'c_id':id}
    return render_template('/videos/videos.html',data=data)
# 添加界面
@video.route('/add_video/<id>')
def add_video(id):#外键id
    print 'id>>>>>>',id
    teachers = db.session.query(Teachers).all()
    teacher = db.session.query(Teachers).first()


    data = {'islogin':session.get('islogin'),'teachers':teachers,'name':teacher.name,'id':id}
    return render_template('/videos/add_video.html',data=data)

# 提交界面
@video.route('/commit_add_video/<id>',methods=['POST'])
def commit_add_video(id):
    print 'id22>>>>>>>>',id,request.form['name'],request.form['msg'],request.form['teacher'],request.form['time']
    c_id = id 
    title = request.form['name']
    hits = 0
    seconds = request.form['time']
    intro = request.form['msg']
    addtime = datetime.datetime.now()
    teacher = db.session.query(Teachers).filter(Teachers.name==request.form['teacher']).first()
    
    t_id = teacher.id
    video = Videos(title=title,c_id=c_id,hits=hits,seconds=seconds,intro=intro,addtime=addtime,t_id=t_id)
    db.session.add(video)
    db.session.commit()
    return 'add video success'
# 视频编辑界面
@video.route('/edite_video/<id>')
def edite_video(id):
    video = db.session.query(Videos).filter(Videos.id==id).first()
    teachers = db.session.query(Teachers).all()
    teacher = db.session.query(Teachers).filter(Teachers.id==video.t_id).first()
    
    data = {'islogin':session.get('islogin'),'teachers':teachers,'name':teacher.name,'id':id,'video':video}

    print 'edite id >>>>>>',id
    return render_template('/videos/edite_video.html',data=data)

# 提交视频编辑界面
@video.route('/commit_edite_video/<id>',methods=['POST'])
def commit_edite_video(id):
    print 'id commit 2>>>>>>>>',id,request.form['name'],request.form['msg'],request.form['teacher'],request.form['time']
    
    title = request.form['name']
    seconds = request.form['time']
    intro = request.form['msg']
    teacher = db.session.query(Teachers).filter(Teachers.name==request.form['teacher']).first()
    
    t_id = teacher.id

    video = db.session.query(Videos).filter(Videos.id==id).first()
    video.title = title
    video.seconds = seconds
    video.intro = intro 
    video.t_id = t_id

    db.session.commit()
    return 'edite video success'


@video.route('/delete_video',methods=['POST'])
def delete_video():
    id = request.form['id']
    print 'delete video id>>>>>',id
    video = db.session.query(Videos).filter(Videos.id==id).first()
    db.session.delete(video)
    db.session.commit()

    return 'success'