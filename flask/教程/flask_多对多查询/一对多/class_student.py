#coding:utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager 
import model
import random
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:123@localhost:3306/test3'

db = SQLAlchemy(app)
manager = Manager(app)

@app.route('/add')
def add():
    # for item in range(10):
    #     name = 'cla_%s' %item
    #     member_c = random.randint(30,100)
    #     cla = model.Classes(name=name,member_c=member_c)
    #     db.session.add(cla)
    # db.session.commit()

    # for item in range(500):
    #     name = 'stu_%s' %item
    #     age = random.randint(20,23)
    #     sex = random.randint(0,1)
    #     # 外键对应着别人的id，不可以是0
    #     class_id = random.randint(1,10)
    #     stu = model.Students(name=name,age=age,sex=sex,class_id=class_id)
    #     db.session.add(stu)
    # db.session.commit()


    # stus = db.session.query(model.Students).filter(model.Students.class_id==5).all()
    # for stu in stus:
    #     print stu.name

    cla = db.session.query(model.Classes).filter(model.Classes.id==1).first()
    # 根据关系查询所有的学生
    students =  cla.students

    for stu in students:
        print stu.name

        # 根据backref反向查询
    # stu = db.session.query(model.Students).filter(model.Students.id==7).first()
    # banji = stu.cla 
    # print banji.name




    return 'add over'


if __name__=='__main__':
    app.debug = True
    manager.run()