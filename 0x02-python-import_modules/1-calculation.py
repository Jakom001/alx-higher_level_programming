#!/usr/bin/python3

if __name__ == " __main__":
    """simple calculator"""
    from calculator_1 import add, sub, mul, div
    a = 1
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".fomat(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
