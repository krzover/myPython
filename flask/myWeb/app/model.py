#coding:utf-8

from . import db
from sqlalchemy.orm import relationship,backref
from werkzeug.security import generate_password_hash,check_password_hash


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(255),nullable=False)
    user_psw = db.Column(db.String(255),nullable=False)

    @property

    def password(self):
        print '<><>不让读取psw<><>'
    @password.setter
    def password(self,psw):
        self.user_psw = generate_password_hash(psw)
    def check_psw(self,psw):
        return check_password_hash(self.user_psw,psw)
    

class Kind(db.Model):
    __tablename__ = 't_kinds'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    course = relationship('Courses',backref='kinds',cascade='delete')

class Courses(db.Model):
    __tablename__ = 't_courses'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    abstract = db.Column(db.String(255))
    addtime = db.Column(db.DateTime)
    k_id = db.Column(db.Integer,db.ForeignKey('t_kinds.id'))
    videos = relationship('Videos',backref='courses',cascade='delete')

class Videos(db.Model):
    __tablename__ = 't_videos'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    time  = db.Column(db.Integer)
    hits = db.Column(db.Integer)
    addtime = db.Column(db.DateTime)
    abstract = db.Column(db.String(255))
    t_id  = db.Column(db.Integer)
    c_id = db.Column(db.Integer,db.ForeignKey('t_courses.id'))

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    abstract = db.Column(db.String(255))
    level = db.Column(db.String(255))