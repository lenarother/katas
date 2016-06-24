"""Test warnings module"""

from warnings import warn


def add(a, b):
    """Adds two numbers"""
    if type(a) == str:
        warn("It might be not really something you want to do")
    result = a + b
    return result


if __name__ == "__main__":
    print(add('3', '2'))
