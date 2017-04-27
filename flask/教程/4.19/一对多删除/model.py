from hello import db 
from sqlalchemy.orm import relationship,backref
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
