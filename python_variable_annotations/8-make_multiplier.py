#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function
    make_multiplier that takes a
    float multiplier as argument and
    returns a function that
    multiplies a float b multiplier.
    """
    def multiply(numb: float) -> float:
        """
        """
        return numb * multiplier
    return multiply
