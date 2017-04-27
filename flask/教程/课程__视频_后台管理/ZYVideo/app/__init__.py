#coding:utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
# generate_password_hash 生成加密的密码
# check_password_hash 验证密码
# from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.debug = True

db = SQLAlchemy()

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/test3'
    app.secret_key = '123'
    db.init_app(app)
    
    # 一定要在这里导入，然后注册到app
    # 从同级目录里面找到main文件夹，导入main对象（在init文件夹里面）
    from .course import course
    app.register_blueprint(course)

    from .auth import auth 
    app.register_blueprint(auth)

    from .videos import video 
    app.register_blueprint(video)

    from .teachers import teacher 
    app.register_blueprint(teacher)

    return app 

