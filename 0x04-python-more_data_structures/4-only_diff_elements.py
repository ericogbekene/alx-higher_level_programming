#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for index in set_1:
        if index not in set_2:
            new_set.add(index)
    for maple in set_2:
        if maple not in set_1:
            new_set.add(maple)
    return new_set
