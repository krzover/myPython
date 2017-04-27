#coding:utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager 
import model
import random,datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/test3'
manager  = Manager(app)
db = SQLAlchemy(app)

@app.route('/add')
def add():
    # for item in range(1,8):
    #     name = 'name_%s' %item
    #     kind = model.Kinds(name=name)
    #     db.session.add(kind)
    #     db.session.commit()

    # for item in range(1,20):
    #     title = 'title_%s' %item 
    #     abstract = '_abstract' * random.randint(1,6)
    #     addtime = datetime.datetime.now()
    #     # 外键范围，从数据库查看，然后在设置
    #     k_id = random.randint(1,7)
    #     course = model.Couses(title=title,abstract=abstract,addtime=addtime,k_id=k_id)
    #     db.session.add(course)
    #     db.session.commit()

    for item in range(1,60):
        title = 'title_%s' %item 
        time = random.randint(400,600)
        hits = random.randint(1000,2000)
        addtime = datetime.datetime.now()
        abstract = 'abstract'*random.randint(6,10)
        t_id  = random.randint(1,8)
        c_id = random.randint(1,19)
        video = model.Videos(title=title,time=time,hits=hits,addtime=addtime,abstract=abstract,t_id=t_id,c_id=c_id)
        db.session.add(video)
        db.session.commit()
    return 'add success'

@app.route('/delete')
def delete():
    kind = db.session.query(model.Kinds).filter(model.Kinds.id==2).first()
    db.session.delete(kind)
    db.session.commit()

    return 'delete success'

if __name__ == '__main__':
    app.debug = True
    manager.run()