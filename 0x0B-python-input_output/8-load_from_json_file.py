#!/usr/bin/python3
"""
this module adds a method that creates an obj from JSON file
"""
import json


def load_from_json_file(filename):
    """ this method creates an obj from JSON file """
    with open(filename) as this_file:
        this_obj = json.load(this_file)
    return this_obj
