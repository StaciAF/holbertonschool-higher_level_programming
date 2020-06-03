#!/usr/bin/python3
"""
this module creates a method to read n lines in a text file
"""


def read_lines(filename="", nb_lines=0):
    """ this method prints n lines of text file to stdout """
    linecount = 0
    with open(filename, encoding="utf-8") as this_file:
        for line in this_file:
            linecount += 1
            print(line, end="")
            if linecount == nb_lines:
                break
