#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(numb: float) -> float:
        """
        """
        return numb * multiplier
    return multiply
