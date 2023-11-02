#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arguments = sys.argv
    len1 = len(arguments) - 1
    result = 0

    for i in range(1, (len1 + 1)):
        result = result + int(arguments[i])
    print("{:d}".format(result))
