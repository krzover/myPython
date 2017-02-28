#coding:utf-8
import json

'''
手机品牌                手机价格      库存数量
     vivoX9                     2798               25
     iphone7(32G)         4888               31
     iphone7(128G)       5668               22
     iphone7P(128G)     6616               29
     iphone6(16G)          3858               14
'''

list = [{'name':'vivo','money':'100','num':'10'},{'name':'iphone','money':'200','num':'15'}]

#输出所有信息
def output_info():
    list = read_info()
    print '\n库存产品如下:'
    for x in xrange(len(list)):
        print 'adr:',x,'品牌:',list[x]['name'],'价格',list[x]['money'],'库存:',list[x]['num']
    print
#写入信息
def write_info(list):
    file = open('phone.txt','w') 
    list = json.dumps(list)
    file.write(list)
    file.close()
#读取信息
def read_info():
    file = open('phone.txt','r') 
    read_content = file.read()
    list = json.loads(read_content)
    file.close()
    return list
# output_info()
# write_info(list)
# read_info()





def main():
    chose =str(raw_input('1.查看所有手机品牌\n2.修改产品库存信息\n3.移除产品库存信息\n4.退出程序\n请选择:'))
    if chose == '1':
        print '<><>chose'
        ####输出所有品牌
        output_info()
        cha_list= read_info()
        check_chose = str(raw_input('1.选择产品序号查看详情\n2.返回\n请选择:'))
        if check_chose=='1':
            cha_adr = input('选择adr_num:')
            
            print 'adr:',cha_adr,'品牌:',cha_list[cha_adr]['name'],'价格',cha_list[cha_adr]['money'],'库存:',cha_list[cha_adr]['num']
            buy_chose = str(raw_input('1.购买\n2.返回\n请选择:'))
            if buy_chose == '1':
                ###购买
                print '扣除',cha_list[cha_adr]['money']
                main()
            else:
                #返回
                main()
        if check_chose=='2':
            main()
    if chose =='2' :
        change_chose = str(raw_input('1.添加新产品\n2.修改原有产品\n请选择:'))
        add_list = read_info()
        if change_chose =='1':
            add_name = str(raw_input('添加品牌:'))
            if len(add_list)>0:
                for x in add_list:
                    if x['name'] == add_name: 
                        print '<><>已经有此品牌.返回'
                        main()
            add_num = raw_input('添加库存:')
            add_money = raw_input('添加价格:')
            add_dic = {'name':add_name,'money':add_money,'num':add_num}
            add_list.append(add_dic)
            write_info(add_list)
            main()
        if change_chose == '2':
            
            ###修改原有产品
            change_sec_chose =str(raw_input('1.根据选择序号进行修改\n2.返回\n请选择:'))
        if change_sec_chose == '1':
            output_info()
            read_list = read_info()
            ###根据选择序号进行修改
            change_adr =int(raw_input('选择序号:'))
            if 0<=change_adr<=len(read_list):
                change_name = raw_input('输入品牌:')
                change_num = raw_input('输入库存:')
                change_money = raw_input('输入价格:')
                change_dic = {'name':change_name,'money':change_money,'num':change_num}

                read_list[change_adr] = change_dic
                write_info(read_list)
                output_info()
                print  '修改完成'
                main()

        if change_sec_chose == '2':
            #返回
            main()
        else:
            print '<><>输出错误.1 添加.2修改'
            main()
    if chose == '3':
        del_chose = str(raw_input('1.查看所有产品\n2.移除所有产品\n3.返回\n请选择:'))
        if del_chose == '1':
            output_info()
            main()
        if del_chose == '2':
            list =[]
            write_info(list)
            main()
        if del_chose == '3':
            #返回
            main()
    if chose == '4':
        ###退出程序
        main()
main()


