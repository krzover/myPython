#coding:utf-8
from orm import db
#  模型类，对应数据库的表
# 所有的模型类必须继承(db.Model)
class Users(db.Model):
    # 定义表名字
    __tablename__ = 'users'

    # id name age sex
    # id代表生成的table的一列，name,age,sex以此类推
    # db.Integer 列的数据类型
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Boolean)
    address = db.Column(db.String(90))