#coding:utf-8

import db_class

while 1:
    db_class.print_info()
    db_admin = db_class.dbManager('database.db','people')
    chose = input('输入命令:')
    if chose == 1:
        print '<>输出所有信息'
        rel = db_admin.list_db()
        for x in rel:
            print u"|id:%d|姓名:%s|性别:%d|年龄:%d|手机号:%d|"%(x[0],x[1],x[2],x[3],x[4])
    elif chose == 2:
        print '<>查找名字'
        name = raw_input('查找名字')
        rel = db_admin.name_find(name)
        for x in rel:
            print u"|id:%d|姓名:%s|性别:%d|年龄:%d|手机号:%d|"%(x[0],x[1],x[2],x[3],x[4])
    elif chose == 3:
        print '<>查找手机号'
        num = raw_input('查找手机号:')
        rel = db_admin.num_find(num)
        for x in rel:
            print u"|id:%d|姓名:%s|性别:%d|年龄:%d|手机号:%d|"%(x[0],x[1],x[2],x[3],x[4])
    elif chose == 4: 
        print '<>添加信息'  
        id = input('id:')
        name = raw_input('name:')
        sex = input('sex:')
        age = input('age:')
        phone = input('phone:')
        human = db_class.people(id,name,sex,age,phone)
        db_admin.insert_people(human)
    elif chose == 5:
        print '<>修改信息'
        change_id = input('change_id:')
        id = None
        name = raw_input('name:')
        sex = input('sex:')
        age = input('age:')
        phone = input('phone:')
        human = db_class.people(id,name,sex,age,phone)
        db_admin.edit_id(change_id,human)
    elif chose == 6:
        print '<>删除id'
        del_id = input('删除id:')
        db_admin.delete_id(del_id)