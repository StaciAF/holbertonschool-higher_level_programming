#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        a1 and a2 = 0
        b1 and b2 = 0
    res = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return (res)
