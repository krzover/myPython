#coding:utf-8
import os
global students_list
students_list = []
def readinfo():
    #读取info.txt内内容
    # students_list = []
    if os.path.exists('info.txt') :
        global students_list
        students_list = []
        open_info = open('info.txt','r')
        lin_add = []
        line_open = open_info.readline()
        while line_open:
            line_open = line_open.strip('\n')
            lin_split = line_open.split(';')
            students_list.append(lin_split)
            print 'read_info_load:',lin_split
            line_open = open_info.readline()
        out_list()
    else:
        print 'no local info.txt'
        main_obj()

#输出大列表内容
def out_list():
    out_one_num = 0
    global students_list
    for out_one in students_list:
        print 'adr:',out_one_num,'name:',out_one[0],'age:',out_one[1],'phone:',out_one[2],'\n'
        #print 'ok,have',len(students_list), 'tudents\n'
        #print 'adr:',out_one_num,'name:',out_one[0],'age:',out_one[1],'phone:',out_one[2],'\n'
        out_one_num = out_one_num+1

def write_info():
    #打开文件开始写入  
    file_w = open('info.txt','a')
    global students_list
    for add_small in students_list:
        w_num = 0
        for info_int in add_small:
            w_num = w_num+1
            info_str = str(info_int)
            file_w.write(info_str)
            if  w_num == 3:
                file_w.write('\n')
            else:
                file_w.write(';')
    students_list = []
    file_w.close()

#输出主菜单
def print_main():
    print '1.add\n2.change\n3.find\n4.dele'

#添加学生
def add_student():
    global students_list
    students_list = []
    add_name = input ('add_name:')
    add_age = input ('add_age:')
    add_phone = input ('add_phone:')
    addput_list = [add_name,add_age,add_phone]
    students_list.append(addput_list)
    print '<><>',students_list
    #执行写入方法
    write_info()
    readinfo()
    print 'ok,have',len(students_list), 'tudents\n'
#修改学生
def change_student ():
    readinfo()
    chose_num = input('chose_change_Num:')
    if len(students_list) !=0 and 0<=chose_num<=len(students_list)-1:
        cha_name = input('change_name:')
        cha_age = input('change_age:')
        cha_phone = input('change_phone:')
        change_list = [cha_name,cha_age,cha_phone]
        students_list[chose_num] = change_list
        #执行写入方法
        os.remove('info.txt')
        write_info()
        print ' ok'
    else:
        print 'NoFind,Try again\n'
#查询学生
def find_student():
    readinfo()
    if len(students_list)>0:
        find_name = input('find_name:')
        find_count = 0
        for find_list in students_list:
            find_count = find_count+1
            find_name = str(find_name)
            if find_name == find_list[0]:
                print 'ok',find_list,'  _adr:',find_count-1
            else:
                print 'no find! _adr:',find_count-1
    else:
        print'no people in list\n' 
#索引删除学生
def del_student():
    print '1.del numn\n 2.del all'
    del_chose = input('chose_del_num:')
    if del_chose == 1:
        readinfo()
        global students_list
        if len(students_list)>0:
            #out_list()
            del_num = input('del_num:')
            if 0<=del_num <=len(students_list)-1:
                del students_list[del_num]
                print 'del ok:\n',out_list(),'\n'
                #执行写入方法
                os.remove('info.txt')
                write_info()
            else:
                print 'no find\n'
        else:
            print 'no people'
    elif del_chose == 2:
        students_list = []
        if os.path.exists('info.txt') :
            #直接删除文件
            os.remove('info.txt')
            print 'clear ok',out_list()
        else:
            print '___no file'
    else:
        print 'input error,try again'
        del_student()
#主程序
def main_obj():
    #out_list()
    print_main()
    main_num = input('chose number:')
    if main_num == 1:
        add_student()
        main_obj()
    elif main_num == 2:
        change_student()
        main_obj()
    elif main_num == 3:
        find_student()
        main_obj()
    elif main_num == 4:
        del_student()
        main_obj()
    elif main_num == 5:
        students_list = []
        readinfo()
        main_obj()
main_obj()
