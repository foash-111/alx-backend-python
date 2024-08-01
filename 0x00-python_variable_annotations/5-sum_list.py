#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """type-annotated sum_list function"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
