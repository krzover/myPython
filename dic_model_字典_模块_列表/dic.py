#coding:utf-8

import model
people_list = []
one_list = []
def main_obj():
    
    main_num = input('\n1.add\n2.change\n3.find\n4.dele\nchose number:')
    if main_num == 1:
        model.add_people(people_list)
        main_obj()
    elif main_num == 2:
        model.change_people(people_list)
        main_obj()
    elif main_num == 3:
        model.find_people(people_list)
        main_obj()
    elif main_num == 4:
        model.dele_people(people_list)
        main_obj()
    elif main_num == 5:
        model.print_people(people_list)        
        main_obj()
main_obj()