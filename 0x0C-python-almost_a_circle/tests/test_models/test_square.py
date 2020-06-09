#!/usr/bin/python3
"""
This module performs unit tests on class Square and all methods,
all must be PEP8 validated
"""
import sys
import os
import io
import unittest
import json
# import pep8
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

#    def test_pep8_style(self):
#        """ test files for pep8 style """
#        pep8style = pep8.StyleGuide(quiet=True)
#        result = pep8style.check.files(['square.py'])
#        self.assertEqual(result.total_errors, 0,
#                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
