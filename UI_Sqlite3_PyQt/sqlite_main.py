#coding:utf-8

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sqlite3
import sqlite_table
import sqlite_class
import sys
import os
class manager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self = uic.loadUi('ui_main.ui',self)        
    def sql_add(self):
        # reload(sqlite_class)
        global add_face
        add_face = sqlite_class.addsql()
        add_face.show()
        self.close()
        

    def sql_change(self):
        print 'change'
        self.close()
        global change_face
        change_face = sqlite_class.changesql()
        change_face.show()

    def sql_find(self):
        print 'find'
        self.close()
        global find_face
        find_face = sqlite_class.findsql()
        find_face.show()

    def sql_del(self):
        print 'del'
        self.close()
        global del_face
        del_face = sqlite_class.delsql()
        del_face.show()
    def lookall(self):
        print 'lookall'
        listt = []
        conn = sqlite3.connect('database.db')  
        sear =  "SELECT * FROM people ORDER BY id ASC"
        idlist = conn.execute(sear)
        for x in idlist:
            listt.append(x)
        global mytable
        mytable = sqlite_table.mytable(listt)
        mytable.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = manager()
    m.show()
    # add_face=None
    sys.exit(app.exec_())