#!/usr/bin/python3

import unittest
from operations import sum, sub, divide
from parameterized import parameterized
import requests
from unittest.mock import patch


def get_url(url):
    resopnse = requests.get(url)
    return resopnse.json()



class TestOperations(unittest.TestCase):


    # @parameterized.expand([
    #     (2, 3, 5),
    #     (3, 4, 7)
    # ])
    # def test_sum(self, a, b, expected):
    #     self.assertEqual(sum(a, b), expected)


        