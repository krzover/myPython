#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import model



app = Flask(__name__)
# config配置信息 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/test3'
# 参照flask-SQLAlchemy 2.1文档连接数据库
# 初始化数据库对象
db = SQLAlchemy(app)
#  管理app，需要通过命令行来运行app或者向数据库导入导入数据
manager = Manager(app)

@app.route('/add')
def add():
    # 创建user的时候，id自增长，不用赋值
    # 给其他属性赋值
    user1 = model.Users(name='ls2',age=12,sex=False)
    user2 = model.Users(name='ls3',age=12,sex=False)
    user3 = model.Users(name='ls4',age=12,sex=False)
    user4 = model.Users(name='ls5',age=12,sex=False)
    user5 = model.Users(name='ls6',age=12,sex=False)
    user6 = model.Users(name='ls7',age=12,sex=False)
    # db.session 数据库回话对象，用来对数据库增删改查
    # db.session.add(user)
    db.session.add_all([user1,user2,user3,user4,user5,user6])
    # 增删改之后需要提交一下
    db.session.commit()

    return 'add success'

@app.route('/query')
def query():
    # all() 是所有数据
    # all_user = db.session.query(model.Users).all()
    

    # 根据id正序，反序查询
    # all_user = db.session.query(model.Users).order_by(-model.Users.id)
   

    # offset 偏移 ；偏移3调数据
    # limit 限制；限制查询20条，如果超过20 ，就查询20条；如果不够20条，有几条查询几条数据
    # all_user = db.session.query(model.Users).offset(3).limit(20)


    #查询第一条数据
    # user = db.session.query(model.Users).first()
    # print user.name


    # filter  根据id 或者 name 或者其他列名进行筛选数据
    # 如果后边有first（） 说明只有一个数据；反之是多个数据
    # all_user = db.session.query(model.Users).filter(model.Users.id==4).first()


    # all_user = model.Users.query.first_or_404()
    
    # page=1  加载第一页
    # per_page=3 每页数据加载三条
    page = model.Users.query.paginate(page=1,per_page=3)
    # page.page 当前页码
    # page.pages 总页数
    # page.total  总的数据条数
    # page.has_next 是否有下一页
    # page.has_prev是否有上一页

    print dir(page),page.page,page.total,page.has_next,page.pages,page.has_prev
    # print all_user.name

    # for item in all_user:
    #     print item.name

    return 'query success'

@app.route('/update')
def update():
    # 获取对象，然后给属性重新复制
    # user = db.session.query(model.Users).first()
    # user.name = '哈哈哈'
    # db.session.commit()

#  这种写法 不能更新数据，删除，添加
    # user = model.Users.query.first()
    
    # print user.name,dir(user)
    # db.session.commit(user)
    return 'update success'

@app.route('/delete')
def delete():

    user = db.session.query(model.Users).first()
    #  在内存中删除
    db.session.delete(user)
    #  把删除结果提交到数据库
    db.session.commit()


    return 'delete/.............'

# 如果表已经生成了，又在model里面添加了字段，这时候提交数据是不会成功
# 这种情况两种解决方案
#1 数据库迁移  Flask-Migrate (2.0.3)
#2 在界面化工具里面手动修改字段
#再添加就成功了
# 更新到指定版本：
 # pip install 文件名==版本号
@app.route('/address')
def address():
    user = model.Users(name='ww',age=30,sex=False,address='henana')
    db.session.add(user)
    db.session.commit()
    return 'address............'

if __name__=='__main__':
    app.debug = True
    manager.run()

    # 指令  python C:\Users\Administrator\Desktop\db\orm.py shell
    # >>> from orm import db
# >>> from model import Users
# 用数据库对象创建所有的表
# >>> db.create_all()
# 删除所有的表
#  db.drop_all()

# orm：  object  relationship  map
# 对象关系映射
# 把数据转化成对象取出来；把对象 转化成数据存进去
# 不用写sql语句  ，代码量少，查询方便