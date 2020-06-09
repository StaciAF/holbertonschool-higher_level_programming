#!/usr/bin/python3
"""
This module performs unit tests on class Base and all methods,
all must be PEP8 validated
"""
import io
import sys
import os
import unittest
from models.base import Base
import json
# import pep8


class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

#    def test_pep8_style(self):
#       """ test files for pep8 style """
#        pep8style = pep8.StyleGuide(quiet=True)
#        result = pep8style.check.files(['models/base.py'])
#        self.assertEqual(result.total_errors, 0,
#                         "Found code style errors (and warnings).")

    def test_Base_id_None(self):
        result = Base(None)
        self.assertEqual(result.id, 1)

    def test_Base_id_multi(self):
        result1 = Base()
        result2 = Base()
        result3 = Base(14)
        result4 = Base(7)
        result5 = Base()
        self.assertEqual(result1.id, 2)
        self.assertEqual(result2.id, 3)
        self.assertEqual(result3.id, 14)
        self.assertEqual(result4.id, 7)
        self.assertEqual(result5.id, 4)

    def test_Base_id_public(self):
        result = Base(9)
        result.id = 3
        self.assertEqual(result.id, 3)

    def test_Base_nb_objects(self):
        result = Base()
        self.assertEqual(result.id, Base._Base__nb_objects)

if __name__ == '__main__':
    unittest.main()
