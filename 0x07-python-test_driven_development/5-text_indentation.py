#!/usr/bin/python3
"""
This module prints text with 2 new lines after each of these characters: . ? :
Input passed as test must be a string
"""


def text_indentation(text):
    """ checks text for type string, adds 2 new lines after each . ? and : """
    str_error = "text must be a string"
    split_str = {46: '.''\n''\n', 63: '?''\n''\n', 58: ':''\n''\n'}
    if isinstance(text, str) is False:
        raise TypeError(str_error)
    if text is None:
        raise TypeError(str_error)
    new_text = (text.translate(split_str))
    print(new_text)
