#coding:utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager,Shell
import model
import random,datetime
from werkzeug.security import check_password_hash,generate_password_hash
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/test3'
manager = Manager(app)
db = SQLAlchemy(app)

'''
进入shell环境 测试代码用的；这种方式创建表不靠谱，我们要通过导入的方式（from xxx import xx）创建表
def make_context():
    d = dict(db=db,Classes=model.Classes,Teachers=model.Teachers,ClassTeacher=model.ClassTeacher)
    return d

manager.add_command('shell',Shell(make_context=make_context))
'''
@app.route('/add')
def add():
    # for item in range(15):
    #     name = 'name_%s' %random.randint(1,15)
    #     num = random.randint(50,100)
    #     # datetime对象
    #     time = datetime.datetime
    #     # time.now() 年月日时分秒
    #     cla = model.Classes(name=name,num=num,addtime=time.now())
    #     db.session.add(cla)
    # db.session.commit()

    # for item in range(1,10):
    #     name = 'name_%s' %random.randint(1,10)
    #     sex = random.randint(0,1)
    #     teacher = model.Teachers(name=name,sex=sex)
    #     db.session.add(teacher)
    # db.session.commit()

    # for item in range(1,10):
    #     cl_id = random.randint(1,15)
    #     tea_id = random.randint(1,10)
    #     # 添加数据的时候，cl_id和tea_id的组合是唯一的，如果出现第二个一样的，就会报错；需要重新运行代码去随机；要么就做判断，如果是重复的就跳过
    #     classteacher = model.ClassTeacher(cl_id=cl_id,tea_id=tea_id)
    #     db.session.add(classteacher)
    # db.session.commit()

# 找到指定的某个班
    # cla = db.session.query(model.Classes).filter(model.Classes.id==6).first()
    # # 一对多
    # classteacher = cla.classteacher
    # for item in classteacher:
    #     #根据backref反向查询
    #     teacher = item.teacher
    #     print teacher.id,teacher.name

    teacher = db.session.query(model.Teachers).filter(model.Teachers.id==7).first()
    classteacher = teacher.classteacher
    for item in classteacher:
        cla = item.cla
        print cla.name,cla.id

    return 'add success '


if __name__ == '__main__':
    app.debug = True
    manager.run()
