#coding:utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
# generate_password_hash 生成加密的密码
# check_password_hash 验证密码
# from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.debug = True
app.secret_key = '\xcd\x1ff?l\xe2\x1f\xce\xe9\x86\x12u\xf6,\xb5\xf3|\x0f\x15\x1f'
db = SQLAlchemy()

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/test4'
    db.init_app(app)
    
    # 一定要在这里导入，然后注册到app
    # 从同级目录里面找到main文件夹，导入main对象（在init文件夹里面）
    from .main import main
    app.register_blueprint(main)

    from .auth import auth 
    app.register_blueprint(auth)


    return app 

