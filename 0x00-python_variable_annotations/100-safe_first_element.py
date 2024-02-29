#!/usr/bin/env python3

""" Duck typed annotations module """

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Duck typed """
    if lst:
        return lst[0]
    else:
        return None
