#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 7


def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx >= len(my_list):
        return
    return my_list[idx]
