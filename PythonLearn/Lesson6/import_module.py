import xmodule
import random


def calc(a: int | float, b: int | float):
    """This func summarize two digits

    Args:
        a (int | float): first argument
        b (int | float): second argument

    Returns:
        Result summarize arguments a + b
        >>> print(calc(4,6))
        >>> 10
    """
    return a+b


print(xmodule.calculate_steel_weight(3, 1, 0.2))
