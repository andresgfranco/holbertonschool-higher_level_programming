#!/usr/bin/python3
"""Module to test the function max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    '''Tests for '6-max_integer.py'.'''
    def test_max_at_the_end(self):
        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

    def test_max_at_the_beginning(self):
        result = max_integer([3, 2, 1])
        self.assertEqual(result, 3)

    def test_max_in_the_middle(self):
        result = max_integer([1, 2, 3, 1, 2])
        self.assertEqual(result, 3)

    def test_one_negative_number_in_the_list(self):
        result = max_integer([1, 2, 3, -1, 2])
        self.assertEqual(result, 3)

    def test_only_negative_numbers(self):
        result = max_integer([-11, -22, -33, -1, -2])
        self.assertEqual(result, -1)

    def test_list_of_one_element(self):
        result = max_integer([3])
        self.assertEqual(result, 3)

    def test_list_is_element(self):
        result = max_integer([])
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
