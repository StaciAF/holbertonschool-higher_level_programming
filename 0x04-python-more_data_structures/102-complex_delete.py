#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        try:
            del a_dictionary[key]
            return a_dictionary
        except KeyError:
            return a_dictionary
