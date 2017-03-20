#coding:utf-8
print '360极速浏览器.lnk'
name_list = []
def star():
    print '1.添加学员\n2.修改学员\n3.查询学员\n4.删除学员\n0.退出程序'
    num_1 = input('chose:')
     #添加学员
    if num_1 == 1 : 
        add_name = input('添加名字:')
        add_tel = input('添加tel:')
        add_qq = input('添加qq:')
        somebody_list = [add_name,add_tel,add_qq]
        name_list.append(somebody_list)
        print '\n添加成功如下\n',name_list,'\n'
        star()
        #修改学员
    elif num_1 == 2:
        num_chose = input('修改索引为:')
        print '你要修改的是',name_list[num_chose]
        change_name = input('修改名字:')
        change_tel = input('修改tel:')
        change_qq = input('修改qq:')
        change_ok = [change_name,change_tel,change_qq]
        name_list[num_chose] = change_ok
        print '\n修改成功如下\n',name_list,'\n'
        star()
        #查询学员
    elif num_1 == 3:
        check_name = input('查找名字:')
        count_num = 0
        #遍历name_list查找名字
        for check_list in name_list:
            if check_list[0] == check_name:
                print '\n查找成功如下索引位置为:',count_num,'\n','name:',check_list[0],'tel:',check_list[1],'qq:',check_list[2],'\n'
            else:
                count_num = count_num+1
                print '没有找到'
        star()
        #删除学员
    else: #num_1 == 4 :
        num_2 = input('1索引位置删除   2按名字删除    3全部删除\n 请选择:')
        if num_2 == 1:
            #按照索引删除
            del_num = input('输入学员索引位置:')
            del  name_list[del_num]
            print '\n删除成功\n',name_list,'\n'
            star()
        elif num_2 == 2:
            #按照名字删除
            del_name = input('输入删除学员名字:')
            del_count = 0
            for del_list in name_list:
                if del_list[0] == del_name:
                    del name_list[del_count]
                    print '\n删除成功\n',name_list,'\n'
                else:
                    print '没有找到该学院'
            star()
        elif num_2 == 3:
            #直接清空
            while len(name_list)>0:
                del name_list[0]
            print '\n清空成功\n',name_list,'\n'
            star()
        else:
            star()
star()