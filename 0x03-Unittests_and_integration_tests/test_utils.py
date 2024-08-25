#!/usr/bin/env python3
"""TESTING module
parctice with parametrization
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """TEST class using unittest module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_test_access_nested_map(self, nested_map: Dict,
                                    path: Tuple[str],
                                    expected: Union[Dict, int]) -> None:
        """using method and test using assert equal"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """handle KeyError raising part"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
