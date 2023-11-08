#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        if count(i) == 1:
            sum += int(i)
        else:
            sum += 0
    return (sum)
