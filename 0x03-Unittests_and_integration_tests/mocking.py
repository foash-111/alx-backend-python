#!/usr/bin/env python3
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized


def get_data(url):
    response = requests.get(url)
    return response.json()

# Patching `requests.get` to mock the API call


class TestGet(unittest.TestCase):
    

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get(self, url, expected):

        with patch('requests.get') as mock_get:
            mock_get.return_value = expected

            result = get_data(url)

            self.assertEqual(result, expected)













class Mocking:
    def foashing(self):
        return "Mahmoud"


person = Mocking()


print(person.foashing())


with patch.object(Mocking, 'foashing', return_value='not original'):
    print(person.foashing())




"""
In summary, 
use patch.object when you want to:
patch an attribute or method of a specific object or class.

Use patch when you want to patch something at a higher level, 
like a function or class in a module.
"""
