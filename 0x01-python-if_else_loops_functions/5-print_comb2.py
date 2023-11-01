#!/usr/bin/python3
for i in range(0, 100):
    if i in range(0, 9):
        print("{}{}{} ".format('0', i, ','), end='')
    else:
        print("{} {}".format(i, ","), end='')
