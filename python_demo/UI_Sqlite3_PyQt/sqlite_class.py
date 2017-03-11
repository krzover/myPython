#coding:utf-8

import sqlite3
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic
import sqlite_main
import sqlite_table
import sys

class person(object):
    """docstring for person"""
    def __init__(self,p_id,p_name,p_age,p_sex,p_phone):
        self.p_id = p_id
        self.p_name = p_name
        self.p_age = p_age
        self.p_sex = p_sex
        self.p_phone = p_phone

class addsql(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self = uic.loadUi('ui_add.ui',self)
    def updata_sql(self):
        print 'updata_sql'
        try:
            if isinstance(int(self.p_id.text()),int) and isinstance(int(self.p_age.text()),int) and isinstance(int(self.p_phone.text()),int):
                print '判断成功'
                addper = person(int(self.p_id.text()),self.p_name.text(),int(self.p_age.text()),int(self.p_sex.text()),int(self.p_phone.text()))
                conn = sqlite3.connect('database.db')
                name_sql = "INSERT INTO people (id,name,sex,age,phone) VALUES (%d,'%s',%d,%d,%d)"%(addper.p_id,addper.p_name,addper.p_sex,addper.p_age,addper.p_phone)
                conn.execute(name_sql)
                conn.commit()
                box  = QMessageBox.question(self,'提示','添加成功',QMessageBox.Yes)
        except Exception, e:
            box  = QMessageBox.question(self,'警告','除姓名外其他为int类型且不为空',QMessageBox.Yes)
    def back_main(self):
        global main_face
        main_face = sqlite_main.manager()
        main_face.show()
        self.close()

class changesql(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self = uic.loadUi('ui_change.ui',self)
    def chasql(self):     
        print 'change_sql'

        try:
            if isinstance(int(self.p_id.text()),int) and isinstance(int(self.p_age.text()),int) and isinstance(int(self.p_phone.text()),int):
                print '判断成功'
                changeper = person(int(self.p_id.text()),self.p_name.text(),int(self.p_age.text()),int(self.p_sex.text()),int(self.p_phone.text()))
                conn = sqlite3.connect('database.db')
                edit_sql = "UPDATE people SET name='%s',sex=%d,age=%d,phone=%d WHERE id=%d"%(changeper.p_name,changeper.p_sex,changeper.p_age,changeper.p_phone,changeper.p_id)
                conn.execute(edit_sql)
                conn.commit()
                box  = QMessageBox.question(self,'提示','修改成功',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        except Exception, e:
            box  = QMessageBox.question(self,'警告','id为int类型且不为空',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
    def back_main(self):
        print 'backmain'
        global main_face
        main_face = sqlite_main.manager()
        main_face.show()
        self.close()
class findsql(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self = uic.loadUi('ui_find.ui',self)
    def find_sql(self):
        if self.radioname.isChecked():
            changeper =self.p_id.text()
            name_sql = "SELECT * FROM people WHERE name LIKE '%%%s%%'"%changeper
            self.find(name_sql)
        if self.radiophone.isChecked():
            print 'phone'
            try:
                changeper =int(self.p_id.text())
            except Exception, e:
                box  = QMessageBox.question(self,'提示','查找内容为int类型',QMessageBox.Yes)
            # changeper =int(self.p_id.text())
            name_sql = "SELECT * FROM people WHERE phone LIKE '%%%d%%'"%changeper
            self.find(name_sql)
    def find(self,sql):
        list=[]
        print 'find'
        # changeper =self.p_id.text()
        # print changeper
        conn = sqlite3.connect('database.db')
        abc=  conn.execute(sql)
        for  x in abc:
            list.append(x)
        if len(list)>0:
            try:
                global mytable
                mytable = sqlite_table.mytable(list)
                mytable.show()
            except Exception, e:
                print e
        else:
            box  = QMessageBox.question(self,'提示','查找内容为空',QMessageBox.Yes)

    def back_main(self):
        print 'backmain'
        global main_face
        main_face = sqlite_main.manager()
        main_face.show()
        self.close()

class delsql(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self = uic.loadUi('ui_del.ui',self)
    def del_sql(self):     
        try:
            if isinstance(int(self.p_id.text()),int):
                list3 = []
                conn = sqlite3.connect('database.db')  
                sear =  "SELECT id FROM people ORDER BY id ASC"
                idlist = conn.execute(sear)
                for x in idlist:
                    list3.append(x[0])
                if int(self.p_id.text()) in list3:
                    print '存在'
                    del_sql = "DELETE  FROM people WHERE id=%d"%int(self.p_id.text())
                    conn.execute(del_sql)
                    conn.commit()
                    box  = QMessageBox.question(self,'提示','删除完成',QMessageBox.Yes)
                else:
                    box2  = QMessageBox.question(self,'提示','此id不存在',QMessageBox.Yes)
        except Exception, e:
            print e
            print '<><><><><><><'
            box  = QMessageBox.question(self,'提示','删除id为int',QMessageBox.Yes)
    def back_main(self):
        print 'backmain'
        global main_face
        main_face = sqlite_main.manager()
        main_face.show()
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = findsql()
    m.show()
    sys.exit(app.exec_())