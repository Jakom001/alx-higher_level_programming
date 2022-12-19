#!/usr/bin/python3

def safe_print_division(a, b):
    """Return the divisoon of a and b"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside Result:{}".format(result))
    return (result)
