#!/usr/bin/python3


def safe_function(fct, *args):
    result = 0
    import sys
    try:
        result = fct(*args)
    except (ZeroDivisionError, IndexError) as exc:
        result = None
        print("Exception: {}".format(exc), file=sys.stderr)
        return result
    return result
