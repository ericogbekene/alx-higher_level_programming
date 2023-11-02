#!/usr/bin/python3
import sys
count = sys.argv
len1 = len(count) - 1
if len1 >= 0:
    if len1 == 0:
        print("{:d} arguments .".format(len1))
    elif len1 == 1:
        print("{:d} argument".format(len1))
        print("{:d} : {}".format(len1, count[1]))
    else:
        print("{:d} arguments :".format(len1))
        for i in range (1, (len1 + 1)):
            print("{:d}: {}".format(i, count[i]))