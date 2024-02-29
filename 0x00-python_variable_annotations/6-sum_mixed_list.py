#!/usr/bin/env python3

"""Sum a list of floats and integers."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of floats and integers."""
    return sum(mxd_lst)
