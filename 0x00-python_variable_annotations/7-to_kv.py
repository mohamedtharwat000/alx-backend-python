#!/usr/bin/env python3

"""Convert a string to a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a string to a tuple."""
    return (k, float(v**2))
