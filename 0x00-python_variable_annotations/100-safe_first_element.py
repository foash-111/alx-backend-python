#!/usr/bin/env python3
"""duck typing"""
from typing import Sequence, Any, Union, Non


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck typing annotation"""
    if lst:
        return lst[0]
    else:
        return None
