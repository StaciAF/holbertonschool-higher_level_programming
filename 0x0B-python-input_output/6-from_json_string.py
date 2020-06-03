#!/usr/bin/python3
"""
this module adds method to return an object represented by JSON string
"""
import json


def from_json_string(my_str):
    """ returns an object represented by JSON string """
    return json.loads(my_str)
