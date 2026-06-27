#!/usr/bin/python3
"""Define a function that checks inheritance."""


def inherits_from(obj, a_class):
    """Return true if obj inherits form a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
