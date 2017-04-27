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
    data = {'islogin':session.get('islogin'),'courses':courses,'kinds':kinds,'current_kind':kind.name}

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