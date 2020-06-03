#!/usr/bin/python3
"""
this module creates a method to read a text file
"""


def read_file(filename=""):
    """ this method reads a text file and prints it to stdout """
    with open(filename, encoding="utf-8") as this_file:
        read_text = this_file.read()
        print(read_text, end="")
