"""
Geometry module for calculating geometric attributes
Classes:
-circle
-rectangle
"""
import math


class Circle:
    def __init__(self, radius: float):
        """
        Constructor
        :param radius: non-negative number (if a negative number is
                        passed in, it will be converted to positive)
        """
        self.radius = abs(radius)

    def __str__(self) -> str:
        """
        Generate formatted string
        :return: formatted representation of circle
        """
        return f"Circle with radius {self.radius}"

    def area(self) -> float:
        """
        Calculate circle area
        :return: non-negative number
        """
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        """
        Calculate circle perimeter
        :return: non-negative number
        """
        return math.pi * self.radius


class Rectangle:
    def __init__(self, length: float, width: float):
        """
        Constructor
        :param length: non-negative number (if a negative number is
                        passed in, it will be converted to positive)
        """
        self.length = abs(length)
        self.width = abs(width)

    def __str__(self) -> str:
        """
        Generate formatted string
        :return: formatted representation of rectangle lengths
        """
        return f"Rectangle with length {self.length} and width{self.width}"

    def area(self) -> float:
        """
        Calculate rectangle area
        :return: non-negative number
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter
        :return: non-negative number
        """
        return (self.length * 2) + (self.width * 2)
