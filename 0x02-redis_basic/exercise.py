#!/usr/bin/env python3
"""
    Redis basic
"""
import sys
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4

import redis

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
        Writing strings to Redis
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrap
            :param self:, args, kwargs
        """
    return wrapper
