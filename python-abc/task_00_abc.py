#!/usr/bin/python3
"""Defining an abstract class Animal"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Base method to be impleminted."""
        pass


class Dog(Animal):
    """A class that inherite from Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """A class that inherite from Animal"""
    def sound(self):
        return "Meow"
