#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    our_list = []
    our_list += my_list
    if idx < 0:
        return our_list
    if idx >= len(my_list):
        return (our_list)
    else:
        new_list = []
        new_list += my_list
        new_list[idx] = element
        return (new_list)
