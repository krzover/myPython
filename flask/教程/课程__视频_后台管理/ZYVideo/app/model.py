from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.orm import relationship,backref
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    hash_psw = db.Column(db.String(255))

    @property
    def psw(self):
        pass
    @psw.setter
    def psw(self,psw):
        self.hash_psw = generate_password_hash(psw)
    def verify_psw(self,psw):
        return check_password_hash(self.hash_psw,psw)

class Teachers(db.Model):
    __tablename__ = 'v_teachers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    position = db.Column(db.String(255))
    intro = db.Column(db.String(255))

class Kinds(db.Model):
    __tablename__ = 'v_kinds'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    courses = relationship('Courses',backref='kinds',cascade='delete')

class Courses(db.Model):
    __tablename__ = 'v_courses'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    k_id = db.Column(db.Integer,db.ForeignKey('v_kinds.id'))
    addtime = db.Column(db.DateTime)
    intro = db.Column(db.String(255))
    videos = relationship('Videos',backref='course',cascade='delete')

class Videos(db.Model):
    __tablename__ = 'v_detail'
    id = db.Column(db.Integer,primary_key=True)
    c_id = db.Column(db.Integer,db.ForeignKey('v_courses.id'))
    title = db.Column(db.String(255))
    hits = db.Column(db.Integer)
    seconds = db.Column(db.Integer)
    intro = db.Column(db.String(255))
    addtime = db.Column(db.DateTime)
    t_id = db.Column(db.Integer)

