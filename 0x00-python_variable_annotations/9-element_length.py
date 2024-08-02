#!/usr/bin/env python3
"""make the func annotation"""
from typing import List, Tuple, TypeVar, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """retrun the len for each element"""
    return [(i, len(i)) for i in lst]
