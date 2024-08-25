#!/usr/bin/env python3
"""TESTING module
parctice with parametrization
"""

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """TEST class using unittest module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_test_access_nested_map(self, nested_map, path, expected):
        """using method and test using assert equal"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
