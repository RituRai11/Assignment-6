"""Tests for the Fibonacci iterable."""

import pytest
from fibonacci import Fibonacci

def test_non_integer_raises_value_error():
    """Test if non-integer input raises ValueError."""
    with pytest.raises(ValueError):
        Fibonacci("ten")

def test_fibonacci_0():
    """Test Fibonacci(0) returns [0]."""
    assert list(Fibonacci(0)) == [0]

def test_fibonacci_1():
    """Test Fibonacci(1) returns [0, 1]."""
    assert list(Fibonacci(1)) == [0, 1]

def test_fibonacci_2():
    """Test Fibonacci(2) returns [0, 1, 1]."""
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_fibonacci_4():
    """Test Fibonacci(4) returns [0, 1, 1, 2, 3]."""
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]

def test_fibonacci_10():
    """Test Fibonacci(10) returns the correct full sequence."""
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fibonacci_negative():
    """Test that negative input returns an empty list."""
    assert not list(Fibonacci(-5))
