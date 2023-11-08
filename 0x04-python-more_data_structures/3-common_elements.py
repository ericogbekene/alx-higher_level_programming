#!/usr/bin/python3
def common_elements(set_1, set_2):
    lay = set()
    for idx in set_1:
        if idx in set_2:
            lay.add(idx)
            return lay
