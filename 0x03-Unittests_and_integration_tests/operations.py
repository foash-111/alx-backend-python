#!/usr/bin/python3

def sum(a, b):
    return a + b


def sub(a, b):
    return a - b

def divide(a, b):
    try:
        return a / b
    except ValueError:
        print("can't divide by zero") 
