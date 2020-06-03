#!/usr/bin/python3
"""
this module adds a method thats writes to text file
"""


def append_write(filename="", text=""):
    """ this method appends string at end of text file, returns chars """
    with open(filename, mode='a', encoding='utf-8') as this_file:
        write_text = this_file.write(text)
        return write_text
