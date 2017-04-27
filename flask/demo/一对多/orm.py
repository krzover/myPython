#coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from random import randint
import model


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/test3'

db = SQLAlchemy(app)
manager = Manager(app)


@app.route('/')
def index():
    return 'login ok'

@app.route('/add')
def add():

    for y in range(1,11):
        c_id = y
        c_name = 'class_%s'%y
        classnum = randint(10,50)
        cla = model.Classes(id=c_id,name=c_name,classNum=classnum)
        db.session.add(cla)
    db.session.commit()


    for x in range(300):
        id = x+1
        name = 'stu_%s'%x
        sex = randint(0,1)
        age = randint(10,30)
        class_id =  randint(1,10)
        stu = model.Students(name = name,sex=sex,age=age,class_id=class_id)
        db.session.add(stu)
    db.session.commit()

    


    return 'add ok'
@app.route('/query')
def query():
    find = db.session.query(model.Classes).filter(model.Classes.id==1).first()
    print '******',find
    # students = find.class_ship
    # for x in students:
    #     print x.name
    return 'query ok'


if __name__ == '__main__':
    app.debug = True
    manager.run()