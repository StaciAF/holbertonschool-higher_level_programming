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
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pep8_style(self):
        """ test files for pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_inheritance(self):
        self.assertIsInstance(Square(4), Base)
        self.assertIsInstance(Square(4), Rectangle)

    def test_arguments(self):
        result6 = Square(4, 7)
        self.assertEqual(result6.width, 4)
        self.assertEqual(result6.size, 4)

        result6 = Square(5, 0, 2, 99)
        self.assertEqual(result6.id, 99)
        self.assertEqual(result6.width, 5)
        self.assertEqual(result6.size, 5)
        self.assertEqual(result6.x, 0)
        self.assertEqual(result6.y, 2)

    def test_validator_TypeErr(self):
        with self.assertRaises(TypeError):
            Square("nine", 0, 2, 99)
        with self.assertRaises(TypeError):
            Square([5, 9], 0, 2, 99)
        with self.assertRaises(TypeError):
            Square((5, 0), 9, 0, 2, 99)

    def test_validator_ValueErr(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -1, 2, 99)
        with self.assertRaises(ValueError):
            Square(5, 0, -2, 99)

    def test_area(self):
        result6 = Square(5, 9)
        self.assertEqual(25, result6.area())
        result7 = Square(2)
        self.assertEqual(4, result7.area())

    def test_display(self):
        pass

    def test_str_rep(self):
        result8 = Square(2, 100, id=99)
        self.assertEqual(Square.__str__(result8),
                         '[Square] (99) 100/0 - 2')

    if __name__ == '__main__':
        unittest.main()
