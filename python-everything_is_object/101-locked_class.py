#!/usr/bin/python3
"""Defines a class whose instances only accept the first_name attribute."""


class LockedClass:
    """Prevent the creation of new instance attributes, except first_name."""

    __slots__ = ["first_name"]
