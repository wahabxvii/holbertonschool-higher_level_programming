#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    t_f_list = []
    for int in range(len(my_list)):
        if my_list[int] % 2 == 0:
            t_f_list.append(True)
        else:
            t_f_list.append(False)
    return t_f_list
