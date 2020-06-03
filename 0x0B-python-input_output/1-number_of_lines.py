#!/usr/bin/python3
"""
this module creates a method to count lines in a text file
"""


def number_of_lines(filename=""):
    """ this method returns the number of lines in a text file """
    linecount = 0
    with open(filename, 'r') as this_file:
        for line in this_file.readlines():
            linecount += 1
    this_file.closed
    return linecount
