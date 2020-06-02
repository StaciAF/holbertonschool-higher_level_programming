#!/usr/bin/python3
"""
this module adds method to return available attributes and methods of an object
"""


def lookup(obj):
    """ method to return atributes and methods of obj """
    return dir(obj)
