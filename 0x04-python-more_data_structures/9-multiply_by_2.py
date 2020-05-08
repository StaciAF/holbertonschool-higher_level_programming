#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDICT = {}
    for key in a_dictionary:
        newDICT[key] = a_dictionary[key] * 2
    return newDICT
