#!/usr/bin/python3
"""
this module creates MyList class that inherits from list
"""


class MyList(list):
    """ new class inherits list """

    def print_sorted(self):
        """ this method prints the list with ascend sort """
        print(sorted(self))
