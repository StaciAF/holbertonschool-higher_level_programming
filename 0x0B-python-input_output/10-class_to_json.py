#!/usr/bin/python3
"""
this module adds a method to return __dict__ description
"""
import json


def class_to_json(obj):
    """ this method returns dict description for JSON serialization of obj """
    return obj.__dict__
