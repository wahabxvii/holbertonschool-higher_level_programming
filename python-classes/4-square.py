#!/usr/bin/python3
"""Define a square class."""


class Square:
    """A class that defines a square by its size."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an intger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of square."""
        return self.__size ** 2
