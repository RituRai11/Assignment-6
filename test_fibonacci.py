import pytest
from fibonacci import Fibonacci

def test_non_integer_raises_value_error():
    with pytest.raises(ValueError):
        Fibonacci("ten")
import pytest
from fibonacci import Fibonacci

def test_non_integer_raises_value_error():
    with pytest.raises(ValueError):
        Fibonacci("ten")

def test_fibonacci_0():
    assert list(Fibonacci(0)) == [0]

def test_fibonacci_1():
    assert list(Fibonacci(1)) == [0, 1]

def test_fibonacci_2():
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_fibonacci_4():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]

def test_fibonacci_10():
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fibonacci_negative():
    assert list(Fibonacci(-5)) == []
