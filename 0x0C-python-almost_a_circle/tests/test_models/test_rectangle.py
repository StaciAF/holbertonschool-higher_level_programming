#!/usr/bin/python3
"""
This module performs unit tests on class Rectangle and all methods,
all must be PEP8 validated
"""
import unittest
import sys
import io
import os
import json
# import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_inheritance(self):
        self.assertIsInstance(Rectangle(4, 6), Base)

    def test_arguments(self):
        result6 = Rectangle(4, 7)
        self.assertEqual(result6.width, 4)
        self.assertEqual(result6.height, 7)

        result6 = Rectangle(5, 9, 0, 2, 99)
        self.assertEqual(result6.id, 99)
        self.assertEqual(result6.width, 5)
        self.assertEqual(result6.height, 9)
        self.assertEqual(result6.x, 0)
        self.assertEqual(result6.y, 2)

    def test_validator_TypeErr(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "nine", 0, 2, 99)
        with self.assertRaises(TypeError):
            Rectangle([5, 9], 0, 2, 99)
        with self.assertRaises(TypeError):
            Rectangle((5, 0), 9, 0, 2, 99)

    def test_validator_ValueErr(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 9, 0, 2, 99)
        with self.assertRaises(ValueError):
            Rectangle(5, -2, 0, 2, 99)
        with self.assertRaises(ValueError):
            Rectangle(5, 9, -1, 2, 99)
        with self.assertRaises(ValueError):
            Rectangle(5, 9, 0, -2, 99)

    def test_area(self):
        result6 = Rectangle(5, 9, 0, 2, 99)
        self.assertEqual(45, result6.area())
        result7 = Rectangle(2, 100)
        self.assertEqual(200, result7.area())

    def test_display(self):
        pass

    def test_str_rep(self):
        result8 = Rectangle(2, 100, id=99)
        self.assertEqual(Rectangle.__str__(result8),
                         '[Rectangle] (99) 0/0 - 2/100')

#    def test_pep8_style(self):
#        """ test files for pep8 style """
#        pep8style = pep8.StyleGuide(quiet=True)
#        result = pep8style.check.files(['rectangle.py'])
#        self.assertEqual(result.total_errors, 0,
#                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
