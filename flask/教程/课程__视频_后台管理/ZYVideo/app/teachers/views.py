#coding:utf-8
from . import teacher
from flask  import request,render_template,session
from ..model import Teachers
from .. import db
@teacher.route('/all_teacher')
def all_teacher():
    teachers = db.session.query(Teachers).all()

    data = {'islogin':session.get('islogin'),'teachers':teachers}
    return render_template('/teachers/teachers.html',data=data)

@teacher.route('/add_teacher')
def add_teacher():
    data = {'islogin':session.get('islogin')}
    return render_template('/teachers/add_teacher.html',data=data)

@teacher.route('/commit_add_teacher',methods=['POST'])
def commit_add_teacher():
    name = request.form['name']
    msg = request.form['msg']
    teacher_kind = request.form['teacher_kind']
    if teacher_kind=='助教':
        teacher_kind = 'position_0'
    else:
        teacher_kind = 'position_1'
    teacher = Teachers(name=name,intro=msg,position=teacher_kind)
    db.session.add(teacher)
    db.session.commit()
    return 'add success'

@teacher.route('/edite_teacher/<id>')
def eidte_teacher(id):
    teacher = db.session.query(Teachers).filter(Teachers.id==id).first()
    teacher_kind = teacher.position
    print 'teacher_kind>>>>>',teacher_kind
    if teacher_kind=='position_0':
        teacher_kind = u'助教'
    else:
        teacher_kind = u'讲师'
    data = {'islogin':session.get('islogin'),'teacher_kind':teacher_kind,'teacher':teacher,'id':id}
    return render_template('/teachers/edite_teacher.html',data=data)

@teacher.route('/commit_edite_teacher/<id>',methods=['POST'])
def commit_edite_teacher(id):
    # print request.form['name'],request.form['msg'],request.form['teacher_kind'],id
    teacher = db.session.query(Teachers).filter(Teachers.id==id).first()
    teacher.name = request.form['name']
    teacher.intro = request.form['msg']
    teacher_kind = request.form['teacher_kind']
    if teacher_kind==u'助教':
        teacher_kind = 'position_0'
    else:
        teacher_kind = 'position_1'
    print 'commit teacher kind>>>>>>',teacher_kind
    teacher.position = teacher_kind
    db.session.commit()
    return 'commit edite success'

@teacher.route('/delete_teacher',methods=['POST'])
def delete_teacher():
    print 'delete teacher id>>>>>>>',request.form['id']
    teacher = db.session.query(Teachers).filter(Teachers.id==request.form['id']).first()
    db.session.delete(teacher)
    db.session.commit()
    return 'success'