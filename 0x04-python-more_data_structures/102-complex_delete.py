#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    try:
        del a_dictionary[value]
        return a_dictionary
    except KeyError:
        return a_dictionary
