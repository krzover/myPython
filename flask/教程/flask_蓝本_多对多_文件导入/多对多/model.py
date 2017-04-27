#coding:utf-8
from test_many import db 
from sqlalchemy.orm import relationship,backref

class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    num = db.Column(db.Integer)
    # date  年月日；time 时分秒
    addtime = db.Column(db.DateTime)
    # relationship 这里面传的是类名，其他位置（ForeignKey）传入的是表名字
    classteacher = relationship('ClassTeacher',backref='cla')

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    sex = db.Column(db.Boolean)
    classteacher = relationship('ClassTeacher',backref='teacher')
# 多对多关系，需要两张表，额外再加一张中间表

class ClassTeacher(db.Model):
    __tablename__ = 'classteacher'
    # 设置了两个主键，叫联合主键，他们俩组合到一起表示唯一
    cl_id = db.Column(db.Integer,db.ForeignKey('classes.id'),primary_key=True)
    tea_id = db.Column(db.Integer,db.ForeignKey('teachers.id'),primary_key=True)
