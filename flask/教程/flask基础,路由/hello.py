#coding:utf-8
from flask import Flask,url_for,request,render_template

app = Flask(__name__)

# 整体叫路由
# @app.route('/')  装饰器（==）
# http://127.0.0.1:5000/index
@app.route('/')
def hello():
    return 'hello every body '


# 变量<username>\，传递到函数里面，函数参数需要一一对应
@app.route('/user/<username>')
def show_name(username):

    return 'username: %s' %username

@app.route('/user/<username>/<psw>')
def login(username,psw):
    return 'name:%s  psw:%s'%(username,psw)


@app.route('/about')
def about_nothing():
    return 'aboute'

@app.route('/indexes')
def indexes():
    # url_for 传入函数名字，但是返回的是函数对应的连接

    # /about
    return url_for('about_nothing')
    # /about?name=zs
    # return url_for('about_nothing',name='zs')
    # /user/ls
    # return   url_for('show_name',username='ls')

@app.route('/register',methods=['GET','POST','PUT'])
def test_register():
    if request.method == 'GET':
        return 'this is get'
    elif request.method == 'PUT':
        return 'this is PUT'
    else:
        return 'this is post'

@app.route('/template_xx')
def template_test():
    path = url_for('static',filename='test.css')
    return render_template('test.html',canshu1='canshu2',lujing=path)

# 渲染界面
@app.route('/upload')
def upload():

    return render_template('upload.html')

# 上传文件
@app.route('/commit',methods=['GET','POST'])
def commit():
    if request.method == 'POST':
        f = request.files['uf']
        f.save('C:\Users\Administrator\Desktop\upload.jpg')
    return 'success'

if __name__ == '__main__':
    # debug=True   进入调试模式，每次保存代码都可以实时加载，不用重启服务器
    app.run(debug=True)

