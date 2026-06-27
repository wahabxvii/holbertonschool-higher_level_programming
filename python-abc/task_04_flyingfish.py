#!/usr/bin/python3
"""Define classes Fish, Bird and FlyingFish."""


class Fish:
    """Fish class."""

    def swim(self):
        """Define swim method."""
        print("The fish is swimming")

    def habitat(self):
        """Define habitat method."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Define fly method."""
        print("The bird is flying")

    def habitat(self):
        """Define habitat method."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class."""

    def swim(self):
        """Swim method."""
        print("The flying fish is swimming!")

    def fly(self):
        """Fly method."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Habitat method."""
        print("The flying fish lives both in water and the sky!")
