#!/usr/bin/env python3


import unittest
from simple_math import add, subtract

class TestCases(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5,6), -1)
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(1, 1), 0)



if __name__ == "__main__":
    unittest.main()
