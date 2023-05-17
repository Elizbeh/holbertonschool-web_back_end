#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(numb: float) -> float:
        """
        A type-annotated function make
        _multiplier that takes a float
        multiplier as argument and
        returns a function tha
        multiplies a float b
        multiplier.
        """
        return numb * multiplier
    return multiply
