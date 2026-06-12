#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    maxinteger = my_list[0]
    for int in my_list:
        if int > maxinteger:
            maxinteger = int
    return maxinteger
