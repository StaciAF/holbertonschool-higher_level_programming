#!/usr/bin/python3
"""
this module creates a method to write a string to text file
"""


def write_file(filename="", text=""):
    """ this method writes string to text file, return chars written """
    with open(filename, mode='w', encoding='utf-8') as this_file:
        write_text = this_file.write(text)
        return write_text
    this_file.close
