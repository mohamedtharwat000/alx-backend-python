#!/usr/bin/env python3

"""Annotate a function's parameters and return value."""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate a function's parameters and return value."""
    return [(i, len(i)) for i in lst]
