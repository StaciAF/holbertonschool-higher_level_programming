#!/usr/bin/python3
"""
this module adds method to return JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """ this method returns JSON rep of a string (obj) """
    return json.dumps(my_obj)
