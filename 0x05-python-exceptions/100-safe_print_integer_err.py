#!/usr/bin/python3


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError as esc:
        print("Exception: {}".format(esc), file=sys.stderr)
        return False
