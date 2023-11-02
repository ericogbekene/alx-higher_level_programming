#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as calculus

    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, calculus.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, calculus.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, calculus.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, calculus.div(a, b)))
