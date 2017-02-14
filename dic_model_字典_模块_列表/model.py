#coding:utf-8


import os


#输出所有人信息
def print_people(people_list):
    if len(people_list)>0:
        print_num = 0
        print '<><>',people_list
        for onelist in people_list:
            one_dic = {}
            # for one_dic in onelist:
            one_dic = onelist[print_num]
            print 'adr:',print_num,'__',onelist  ,'___print_people'      
            print_name = one_dic.get('name')            
            print_age =one_dic.get('age')            
            print_tel =one_dic.get('tel')  
            print_num+=1           
            #print 'adr:',print_num,'name:',print_name,'age:',print_age,'tel:',print_tel
    else:
        print '<><>None'
    #增加学生
def add_people(people_list):
    add_name = input('add_name:')
    add_age = input('add_age:')
    add_tel = input('add_tel:')
    #添加到字典
    people_name_dic = {'name':add_name}
    people_age_dic = {'age':add_age}
    people_tel_dic = {'tel':add_tel}
    #输入信息得到的字典然后添加到列表中
    one_list = []
    one_list.append (people_name_dic)
    one_list.append (people_age_dic)
    one_list.append (people_tel_dic)
    people_list.append(one_list)
#修改学生
def change_people(people_list):
    #输出所有人信息
    print_people(people_list)
    #选择索引修改
    change_num = input('change_num:')
    if 0<=change_num<=len(people_list) and len(people_list)!=0:        
        change_name = input('change_name:')
        change_age = input('change_age:')
        change_tel = input('change_tel:')

        people_list[change_num] = [{'name':change_name},{'age':change_age},{'tel':change_tel}]
        print 'change ok___',people_list
    else:
        print 'error change_num'
        return
#查找学生
def  find_people(people_list):
    find_name = input('find_name:')
    find_list = []
    find_dic = {}
    for find_list in people_list:
        find_dic = find_list[0]
        if find_dic.get('name') == find_name:
            print 'find ok___',find_list
            print 'name:',find_list[0]['name'],'age:',find_list[1]['age'],'tel:',find_list[2]['tel']
        else:
            print 'None'
#删除学生
def dele_people(people_list):
    print_people(people_list)
    chose_num = input('\n1.del_num\n2.del_all\nchose_num:')
    if chose_num == 1:
        chose_del = input('num:')
        del people_list[chose_del]
        print_people(people_list)
    if chose_num == 2:
        #不能直接置空(类似双指针问题)
        while  len(people_list)>0:
            del people_list[0]
        print_people(people_list)
        
    else:
        print 'error num'
    return