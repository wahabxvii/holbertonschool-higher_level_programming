#!/usr/bin/python3
"""Define a BaseGeometry class."""


class BaseGeometry:
    """A class with area method."""
    def area(self):
        """Raises an exeption that area is not implemented."""
        raise Exception("area() is not implemented")
