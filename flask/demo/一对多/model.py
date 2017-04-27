#coding:utf-8


from sqlalchemy.orm import relationship,backref
from orm import db



class Classes(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    classNum = db.Column(db.Integer)
    class_ship = relationship('Students',backref = 'cla')

class Students(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    sex = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    class_id = db.Column(db.Integer,db.ForeignKey('class.id'))