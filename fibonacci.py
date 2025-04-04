"""Module for Fibonacci iterable class."""
class Fibonacci:
    """An iterable class that generates the Fibonacci sequence up to n terms."""
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        self.n = n
        self.index = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 0 or self.index > self.n:
            raise StopIteration
        if self.index == 0:
            self.index += 1
            return 0
        elif self.index == 1:
            self.index += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            result = self.b
            self.index += 1
            return result
