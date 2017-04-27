#coding:utf-8
from flask import Flask,request,render_template

app = Flask(__name__)

#  路由里面的函数必须有返回值，要么是字符串，要么是模板
#get请求的url的结构   http://127.0.0.1:5000/login?name=zs&psw=123
@app.route('/login')
def login():
       
    return render_template('login.html')

@app.route('/commit',methods=['GET','POST'])
def commit():
    # request  请求上下文
    # request.args 只能获取get请求的参数
    # request.form  请求是post的时候，获取到的表单里面的参数
    # files  args form base_url  values  host_url
    # print '>>>>>>>>>',request.args,request.form,request.values,dir(request)
    print '>>>>>',request.form['name'],request.form['psw']
    name = request.form['name']
    psw = request.form['psw']
    if name == 'zs' and psw == '123':
        return 'login success'
    else:
        return 'login failed'



    return 'success'


if __name__ == '__main__':
    app.run(debug=True)