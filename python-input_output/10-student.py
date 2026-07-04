#!/usr/bin/python3
"""Defines a Student class."""


class Student:



    def __init__(self, first_name, last_name, age):
        """Initialize Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary of a Student instance."""
        dict = {}
        if attrs is None:
            return self.__dict__
        for element in attrs:
            if element in self.__dict__:
                dict[element] = self.__dict__[element]
        return dict
