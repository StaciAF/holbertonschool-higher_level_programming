#!/usr/bin/python3
"""
this module adds method to write object to text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ this method writes an object to a text file """
    with open(filename, 'w') as json_file:
        written = json_file.write(json.dumps(my_obj))
        return written
