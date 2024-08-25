from unittest import TestCase
from math_op import multiply, divide
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


# ////////////////////////////////////////////

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
       

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
