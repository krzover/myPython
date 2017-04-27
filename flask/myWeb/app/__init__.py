#coding:utf-8

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 

import random,datetime

app = Flask(__name__)
app.debug = True
app.secret_key = "'\xc2V\x0f\xb5f\r?\xf8\x9d\x98d\x88\xcb\xc8\x8fz6.U\x1d\xbd\xe5\xfb\x17'"
db = SQLAlchemy(app)

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/try1'

    from .auth import auth
    app.register_blueprint(auth)
    from .main import main
    app.register_blueprint(main)
    from .video import video 
    app.register_blueprint(video)
    
    return app



@app.route('/addmysqldata')
def add():
    from . import model

    for item in range(1,8):
        name = 't_%s' %item 
        abstract = 't_abstract'* random.randint(1,10)
        num = random.randint(0,1)
        level = ''
        if num==0:
            level = '助教'
        else:
            level = '讲师'
        teacher = model.Teachers(name=name,abstract=abstract,level=level)
        db.session.add(teacher)
    db.session.commit()

    # for x in range(1,8):
    #     name = 'name_%s'%x
    #     kind = model.Kind(name = name)
    #     db.session.add(kind)
    # db.session.commit()

    # for x in range(1,20):
    #     title = 'title_%s'%x
    #     abstract = '_abstract'*random.randint(1,5)
    #     addtime = datetime.datetime.now()
    #     k_id = random.randint(1,7)
    #     course = model.Courses(title=title,abstract=abstract,addtime=addtime,k_id=k_id)
    #     db.session.add(course)
    # db.session.commit()

    # for x in range(1,60):
    #     title = 'title_%s'%x
    #     time = random.randint(100,200)
    #     hits = random.randint(500,900)
    #     addtime = datetime.datetime.now()
    #     abstract = '_abstract'*random.randint(3,6)
    #     t_id = random.randint(1,8)
    #     c_id = random.randint(1,9)
    #     video = model.Videos(title=title,time=time,hits=hits,addtime=addtime,abstract=abstract,t_id=t_id,c_id=c_id)
    #     db.session.add(video)
    # db.session.commit()
    return 'ok'