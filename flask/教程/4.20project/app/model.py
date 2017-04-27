#coding:utf-8
from . import db 
from sqlalchemy.orm import relationship,backref
from werkzeug.security import generate_password_hash,check_password_hash
class Users(db.Model):
    __tablename__ = 'users2'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    hash_psw = db.Column(db.String(255))
    # password = '123'
    # 把函数变成属性
    @property
    def password(self):
        # 调用这个不让读取
        pass 
    # 属性赋值的时候会调用set方法
    @password.setter
    # psw 路由里面传过来的psw
    def password(self,psw):
        self.hash_psw = generate_password_hash(psw)
    def verify_psw(self,psw):
        return check_password_hash(self.hash_psw,psw)

# cascade='delete'

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    abstract = db.Column(db.String(255))
    level = db.Column(db.String(255))

class Kinds(db.Model):
    __tablename__ = 't_kinds'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    couses = relationship('Couses',backref='kinds',cascade='delete')

class Couses(db.Model):
    __tablename__ = 't_courses'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    abstract = db.Column(db.String(255))
    addtime = db.Column(db.DateTime)
    k_id = db.Column(db.Integer,db.ForeignKey('t_kinds.id'))
    # cascade='delete'  一对多关系中，父表数据删除，字表也跟着删除  
    videos = relationship('Videos',backref='courses',cascade='delete')

class Videos(db.Model):
    __tablename__ = 't_videos'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    time = db.Column(db.Integer)
    hits = db.Column(db.Integer)
    addtime = db.Column(db.DateTime)
    abstract = db.Column(db.String(255))
    t_id = db.Column(db.Integer)
    c_id = db.Column(db.Integer,db.ForeignKey('t_courses.id'))