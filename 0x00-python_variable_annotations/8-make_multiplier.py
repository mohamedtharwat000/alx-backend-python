#!/usr/bin/env python3

"""Make a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make a multiplier function."""
    def multiply(n: float) -> float:
        """Multiply a float by a multiplier."""
        return n * multiplier
    return multiply
