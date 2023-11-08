#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_sort = sorted(a_dictionary.items())
    for key, value in my_sort:
        print('{}: {}'.format(key, value))
