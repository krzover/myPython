#coding:utf-8
----------------------------入口文件------------------------------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from random import randint
import model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/testa'
db = SQLAlchemy(app)
manager = Manager(app)

@app.route('/add')
def add():
    for item in range(100):
        title = 'title_%s'%item
        price = '$%s'%randint(200,1000)
        store = randint(1,100)
        info = 'info%s'%randint(1,100)
        goods = model.Goodsdetail(title = title,price = price,store = store,info = info)
        # INSERT INTO goodsdetail (title, price, anum, info) VALUES (%s, %s, %s, %s)        
        db.session.add(goods)
    db.session.commit()
    return 'add ok'



if __name__=='__main__':
    app.debug = True
    manager.run()


------------------------------------model文件----------------------------

from goods import db

class Goodsdetail(db.Model):
    __tablename__ = 'goodsdetail'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    price = db.Column(db.String(20))
    store = db.Column(db.Integer)
    info = db.Column(db.String(255))





# 指令  python C:\Users\Administrator\Desktop\db\orm.py shell
# >>> from orm import db
# >>> from model import Users
# >>> db.create_all()