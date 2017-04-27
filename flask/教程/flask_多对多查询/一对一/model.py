#coding:utf-8
from class_student import db 
# relationship 建立关系，backref用来反向查询
from sqlalchemy.orm import relationship,backref

class Classes(db.Model):
    __tablename__ = 'classes'
    # id name member_c 
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    # 班级人数
    member_c = db.Column(db.Integer)
    #  一对一，一对多的却别，就是设置uselist=False，那么查询的时候返回结果只有一个
    students = relationship('Students',backref='cla',uselist=False)

    

class Students(db.Model):
    __tablename__ = 'students'
    # id name age sex 
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    sex = db.Column(db.Boolean)
    # 设置外键；classes.id 表名
    class_id = db.Column(db.Integer,db.ForeignKey('classes.id'))