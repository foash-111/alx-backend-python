from unittest import TestCase
from math_op import multiply
from parameterized import parameterized

class TestOperations(TestCase):

    @parameterized.expand([
            (2, 3, 6),
            (3, 4, 12),
            (-2, -5, 10)
    ])
    def test_multiply(self, a, b, expected):
        result = multiply(a, b)
        self.assertEqual(result, expected)
