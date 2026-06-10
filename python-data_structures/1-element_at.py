#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return
    if idx > len(my_list):
        return
    print("Element at index {0:d} is {1:d}".format(idx, my_list[idx]))
