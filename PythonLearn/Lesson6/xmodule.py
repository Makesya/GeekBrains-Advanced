"""
This module contains custom functions for basic arithmetic operations.
"""

__start_sum = 0
__start_mult = 1
__beginning = 0
__continuation = 1

__all__ = ['add', 'subtract', 'divide', 'multiply']


def add(a: int | float, b: int | float) -> int | float:
    """
    This function takes two numbers as input and returns their sum.

    :param a: The first number.
    :param b: The second number.
    :return: The sum of the two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """
    This function takes two numbers as input and returns their difference.

    :param a: The first number.
    :param b: The second number.
    :return: The difference between the two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a - b


def divide(a: int | float, b: int | float) -> int | float:
    """
    This function takes two numbers as input and returns their quotient.

    :param a: The first number.
    :param b: The second number.
    :return: The quotient of the two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def multiply(a: int | float, b: int | float) -> int | float:
    """
    This function takes two numbers as input and returns their product.

    :param a: The first number.
    :param b: The second number.
    :return: The product of the two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a * b


def calculate_steel_weight(length: int | float, width: int | float,
                           height: int | float, density: int | float = 7.85) -> float:
    """This function calculates the weight of a steel object given its dimensions and density.

    Args:
        length (int | float): The length of the steel object.
        width (int | float): The width of the steel object.
        height (int | float): The height of the steel object.
        density (int | float, optional): The density of the steel. Default is 7.85 g/cm^3.

    Raises:
        TypeError: All inputs must be numbers.
        ValueError: Density must be a positive number.

    Returns:
        float: The weight of the steel object in grams.
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("All inputs must be numbers.")
    if density < 0:
        raise ValueError("Density must be a positive number.")
    volume = length * width * height
    weight = volume * density
    return weight
