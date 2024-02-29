#!/usr/bin/env python3

""" TypeVar """

from typing import Mapping, TypeVar, Union, Any, Optional

T = TypeVar('T')
D = Mapping


def safely_get_value(dct: D, key: Any, default: Optional[T]) -> Union[Any, T]:
    """ doc """
    if key in dct:
        return dct[key]
    else:
        return default
