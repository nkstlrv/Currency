from typing import Any
import requests
import pytest


def func(a: Any):
    return a


def test_func_valid_data():
    test_value1 = 2
    test_value2 = -2
    test_value3 = "Hello"
    test_value4 = True
    test_value5 = [1, 2, 3]

    result1 = func(test_value1)
    result2 = func(test_value2)
    result3 = func(test_value3)
    result4 = func(test_value4)
    result5 = func(test_value5)

    assert result1 == 2
    assert result2 == -2
    assert result3 == "Hello"
    assert result4 is True
    assert result5 == [1, 2, 3]


def test_google():
    url = "https://google.com"
    response = requests.get(url)
    assert response.status_code == 200
