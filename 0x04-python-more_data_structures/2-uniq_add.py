#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    my_set = set()
    for i in my_list:
        my_set.add(i)
    new_list = list(my_set)
    result = sum(new_list)
    return (result)
