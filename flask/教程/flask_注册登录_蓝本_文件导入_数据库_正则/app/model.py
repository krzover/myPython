#coding:utf-8
from . import db 
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

