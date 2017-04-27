#coding:utf-8
# 根据蓝本设置路由
from . import course
from flask import render_template,url_for,request,session,request,redirect
from .. import db
from ..model import Users,Teachers,Kinds,Courses,Videos
import random,datetime
@course.route('/add')
def add():
    # for item in range(1,10):
    #     name = '%s_t_name' %random.randint(1,10)
    #     position = 'position_%s' %random.randint(0,1)
    #     intro = 'inro_' * random.randint(1,20)
    #     teacher = Teachers(name=name,position=position,intro=intro)
    #     db.session.add(teacher)
    #     db.session.commit()


    # for item in range(1,8):
    #     name = 'course_%s' %item
    #     kind = Kinds(name=name)
    #     db.session.add(kind)
    #     db.session.commit()

    # for item in range(1,30):
    #     name = 'name_%s' %item
    #     k_id = random.randint(1,7)
    #     addtime = datetime.datetime
    #     intro = 'intro_'*random.randint(1,20)
    #     course = Courses(name=name,k_id=k_id,addtime=addtime.now(),intro=intro)
    #     db.session.add(course)
    #     db.session.commit()

    # for item in range(1,100):
    #     c_id = random.randint(1,29)
    #     title = 'title_%s' %random.randint(1,100)
    #     hits = random.randint(1,1000)
    #     seconds = random.randint(5000,9000)
    # t_id = random.randint(1,9)
    #     intro = 'video_inro' * random.randint(1,10)
    #     addtime = datetime.datetime
    #     video = Videos(name=name,c_id=c_id,title=title,hits=hits,seconds=seconds,intro=intro,addtime=addtime.now(),t_id=t_id)
    #     db.session.add(video)
    #     db.session.commit()


    return 'add success'

@course.route('/delete')
def  delete():
    # kind = db.session.query(Kinds).filter(Kinds.id==1).first()
    # db.session.delete(kind)
    # db.session.commit()
    return 'delete................'

# 课程列表
@course.route('/<name>')
def mycourse(name):

    if name=='course':
        # 如果输入的是coursename默认加载第一个
        first = db.session.query(Kinds).filter(Kinds.id==1).first()
    else:
        first = db.session.query(Kinds).filter(Kinds.name==name).first()
    # 所有数据
    kinds = db.session.query(Kinds).all()
    print'first111>>>>>>>>>>>',first

    data = {'islogin':session.get('islogin'),'courses':first.courses,'kinds':kinds,'name':first.name,'id':first.id}
    return render_template('/course/course.html',data=data)
# 删除课程
@course.route('/delete_course',methods=['POST'])
def delete_course():
    print '>>>>>>>>>>',request.form
    course = db.session.query(Courses).filter(Courses.id==request.form['id']).first()
    db.session.delete(course)
    db.session.commit()
    return 'success'

# 添加课程
@course.route('/add_course/<id>')
def add_course(id):
    print 'id>>>>',id
    data = {'islogin':session.get('islogin'),'id':id}
    return render_template('/course/add_course.html',data=data)

# 添加的课程
@course.route('/commit_course/<id>',methods=['POST'])
def commit_course(id):
    name = request.form['name']
    msg = request.form['msg']
    time = datetime.datetime.now()
    course = Courses(name=name,addtime=time,k_id=id,intro=msg)
    db.session.add(course)
    db.session.commit()

    return 'add success'
# 编辑课程
@course.route('/edite_course/<id>')
def edite_course(id):
    course = db.session.query(Courses).filter(Courses.id==id).first()
    data = {'islogin':session.get('islogin'),'course':course}
    return  render_template('/course/edite_course.html',data=data)
# 提交编辑的课程
@course.route('/commit_edite_course/<id>',methods=['POST'])
def commit_edite_course(id):
    print '>>>>>>>',id,request.form['name'],request.form['msg']
    course = db.session.query(Courses).filter(Courses.id==id).first()
    course.name = request.form['name']
    course.intro = request.form['msg']
    db.session.commit()
    return 'commit_edite_course success'