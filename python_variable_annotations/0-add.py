#!/usr/bin/env python3


def add(a: float, b: float) -> float:
    return a + b


print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
