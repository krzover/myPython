#coding:utf-8

import sqlite3

def print_info():
    print
    print '命令列表：'
    print '1--list                 列出所有人,，可简写为ls'
    print '2--find name      按姓名查找，支持模糊查找'
    print '3--find number   按手机号查找，支持模糊查找'
    print '4--add                 添加 '
    print '5--edit id              修改指定id的数据'
    print '6--delete id          删除指定id，可简写为del id'
    print '7--help                 显示命令列表'
def for_rel(rel):
    for x in rel:
            print u"|id:%d|姓名:%s|性别:%d|年龄:%d|手机号:%d|"%(x[0],x[1],x[2],x[3],x[4])
class people(object):
    """docstring for people"""
    def __init__(self,id,name,sex,age,phone):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.phone = phone

class dbManager(object):
    """docstring for dbMag"""
    def __init__(self,db_path,db_table):
        self.db_path = db_path
        self.db_table = db_table
    
    def connect_sql(self):
        return sqlite3.connect(self.db_path)
    def list_db(self):
        conn = self.connect_sql()
        list_table = "SELECT id,name,sex,age,phone FROM people ORDER BY id ASC"
        rel = conn.execute(list_table)
        return rel
    def name_find(self,name):
        conn = self.connect_sql()
        name_sql = "SELECT * FROM people WHERE name LIKE '%s%%'"%name
        return conn.execute(name_sql)
    def num_find(self,num):
        conn = self.connect_sql()
        name_sql = "SELECT * FROM people WHERE phone LIKE '%s%%'"%num
        return conn.execute(name_sql)
    def insert_people(self,human):
        conn = self.connect_sql()
        name_sql = "INSERT INTO people (id,name,sex,age,phone) VALUES (%d,'%s',%d,%d,%d)"%(human.id,human.name,human.sex,human.age,human.phone)
        #如果id重复.自动按照id顺序添加
        try:
            conn.execute(name_sql)
            conn.commit()
        except Exception, e:
            print 'id不可重复,自动按照id顺序添加'
        finally:
            rel = self.list_db()
            for x in rel:
                a=x[0]+1
            name_sql = "INSERT INTO people (id,name,sex,age,phone) VALUES (%d,'%s',%d,%d,%d)"%(a,human.name,human.sex,human.age,human.phone)
            conn.execute(name_sql)
            conn.commit()
        
    def edit_id(self,change_id,human):
        conn = self.connect_sql()
        edit_sql = "UPDATE people SET name='%s',sex=%d,age=%d,phone=%d WHERE id=%d"%(human.name,human.sex,human.age,human.phone,change_id)
        conn.execute(edit_sql)
        conn.commit()
    def delete_id(self,del_id):
        conn = self.connect_sql()
        del_sql = "DELETE FROM people WHERE id=%d"%(del_id)
        conn.execute(del_sql)
        conn.commit()        