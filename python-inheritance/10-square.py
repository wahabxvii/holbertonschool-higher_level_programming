#!/usr/bin/python3
"""Define a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherets from Rectangle."""

    def __init__(self, size):
        """Initialize with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of Square."""
        return self.__size * self.__size
