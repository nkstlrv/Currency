import pytest


def func(a: int):
    return a


def test():
    test_value = 2
    result = func(test_value)
    assert result == 2
