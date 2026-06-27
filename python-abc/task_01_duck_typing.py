#!/usr/bin/python3
"""Define an abstract class."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class."""

    @abstractmethod
    def area(self):
        """Abstract method."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method."""
        pass

class Circle(Shape):
    """A class that inherit from Shape."""

    def __init__(self, radius):
        """Initiate Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of Circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter of Circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A class that inherite from Shape."""

    def __init__(self, width, height):
        """Initiate Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of Rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Prints shape area and perimeter."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
