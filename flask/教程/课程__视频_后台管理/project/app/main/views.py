#coding:utf-8
# 根据蓝本设置路由
from . import main
from flask import render_template,redirect,url_for,request,session
from .. import db 
from ..model import Teachers,Kinds,Couses,Videos
import random,datetime
# 装饰器 不是app.route,变成了main
@main.route('/<name>')
def index(name):
    
    kinds = db.session.query(Kinds).all()
    kind = ''
    if name=='course':

    # 先查询当前分类的内容
        kind = db.session.query(Kinds).first()
    else:
        kind = db.session.query(Kinds).filter(Kinds.name==name).first()
    # 根据分类查询包含的课程
    courses = kind.couses
    # 封装数据源
    data = {'islogin':session.get('islogin'),'courses':courses,'kinds':kinds,'current_kind':kind.name,'id':kind.id}

    # 如果加载的有js文件，那么项目文件的路径里面不能有中文，否则加载不出来
    return render_template('index.html',data=data)

# @main.route('/index/<name>')
# def current_index(name):
    
#     kinds = db.session.query(Kinds).all()
#     courses = kind.couses
#     data = {'islogin':session.get('islogin'),'courses':courses,'kinds':kinds,'current_kind':kind.name}
#     return render_template('index.html',data=data)

@main.route('/commit_delete_course',methods=['POST'])
def commit_delete_course():
    id = request.form['id']
    course = db.session.query(Couses).filter(Couses.id==id).first()
    db.session.delete(course)
    db.session.commit()
    return 'success'


# 添加课程界面
@main.route('/add_course/<id>')
def add_course(id):
    print 'course id>>>>>>>>>',id
    data = {'islogin':session.get('islogin'),'id':id}
    return render_template('add_course.html',data=data)

# 提交 添加课程
@main.route('/commit_add_course/<id>',methods=['POST'])
def commit_add_course(id):
    name = request.form['name']
    msg = request.form['msg']
    # print name,msg,id
    time = datetime.datetime.now()
    course = Couses(title=name,abstract=msg,k_id=id,addtime=time)
    db.session.add(course)
    db.session.commit()

    return 'commit add course succe '

# 课程的编辑
@main.route('/edite_course/<id>')
def edite_course(id):

    course = db.session.query(Couses).filter(Couses.id==id).first()

    data = {'islogin':session.get('islogin'),'course':course}
    return render_template('edite_course.html',data = data)

# 提交编辑课程
@main.route('/commit_edite_course/<id>',methods=['POST'])
def commit_edite_course(id):
    name = request.form['name']
    msg = request.form['msg']
    # print name,msg,id
    course = db.session.query(Couses).filter(Couses.id==id).first()
    course.title = name 
    course.abstract = msg
    db.session.commit()
    return 'commit edite success'

# 视频列表
@main.route('/all_videos/<id>')
def all_videos(id):
    # id 是coourse的id，对应videos的外键
    # print 'course id>>>>>>>>>',id
    l = []
    videos = db.session.query(Videos).filter(Videos.c_id==id).all()
    for item in videos:

        teacher = db.session.query(Teachers).filter(Teachers.id==item.t_id).first()
        l.append(teacher.name)
    data = {'islogin':session.get('islogin'),'videos':videos,'teachers':l,'id':id}
    return render_template('videos.html',data=data)

# 添加视频的界面
@main.route('/add_video/<id>')
def add_video(id):
    #  课程id  ，所有教师
    teachers = db.session.query(Teachers).all()
    teacher = db.session.query(Teachers).first()

    data = {'islogin':session.get('islogin'),'id':id,'teachers':teachers,'name':teacher.name}
    return render_template('add_video.html',data=data)

# 提交添加的视频
@main.route('/commit_add_video/<id>',methods=['POST'])
def commit_add_video(id):
    title = request.form['name']
    abstract = request.form['msg']
    teachername = request.form['teachername']
# 根据名字找到教师，设置id，添加视频
    teacher = db.session.query(Teachers).filter(Teachers.name==teachername).first()
    time = request.form['time']
    # print title,abstract,teachername,time,id
    addtime = datetime.datetime.now()
    video = Videos(title=title,abstract=abstract,t_id=teacher.id,time=time,addtime=addtime,c_id=id,hits=0)
    db.session.add(video)
    db.session.commit()

    return 'add video success'










# 1 根据分类添加课程，传id（以变量的形式）
# 2 根据当前课程id修改课程
# 3 根据课程查询对应的视频，传id，根据外键查询所有视频

# 在一个 for 循环块中你可以访问这些特殊的变量:
# 变量  描述
# loop.index  当前循环迭代的次数（从 1 开始）
# loop.index0     当前循环迭代的次数（从 0 开始）
# loop.revindex   到循环结束需要迭代的次数（从 1 开始）
# loop.revindex0  到循环结束需要迭代的次数（从 0 开始）
# loop.first  如果是第一次迭代，为 True 。
# loop.last   如果是最后一次迭代，为 True 。
# loop.length     序列中的项目数。
# loop.cycle  在一串序列间期取值的辅助函数。见下面的解释。


@main.route('/add')
def add():
    # for item in range(1,8):
    #     name = 't_%s' %item 
    #     abstract = 't_abstract'* random.randint(1,10)
    #     num = random.randint(0,1)
    #     level = ''
    #     if num==0:
    #         level = '助教'
    #     else:
    #         level = '讲师'
    #     teacher = Teachers(name=name,abstract=abstract,level=level)
    #     db.session.add(teacher)
    #     db.session.commit()


    # for item in range(1,8):
    #     name = 'name_%s' %item
    #     kind = Kinds(name=name)
    #     db.session.add(kind)
    #     db.session.commit()

    # for item in range(1,20):
    #     title = 'title_%s' %item 
    #     abstract = '_abstract' * random.randint(1,6)
    #     addtime = datetime.datetime.now()
    #     # 外键范围，从数据库查看，然后在设置
    #     k_id = random.randint(1,7)
    #     course = Couses(title=title,abstract=abstract,addtime=addtime,k_id=k_id)
    #     db.session.add(course)
    #     db.session.commit()

    # for item in range(1,60):
    #     title = 'title_%s' %item 
    #     time = random.randint(400,600)
    #     hits = random.randint(1000,2000)
    #     addtime = datetime.datetime.now()
    #     abstract = 'abstract'*random.randint(6,10)
    #     t_id  = random.randint(1,8)
    #     c_id = random.randint(1,19)
    #     video = Videos(title=title,time=time,hits=hits,addtime=addtime,abstract=abstract,t_id=t_id,c_id=c_id)
    #     db.session.add(video)
    #     db.session.commit()
    return 'add success'