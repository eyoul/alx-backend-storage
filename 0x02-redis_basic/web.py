#!/usr/bin/env python3
""" exercise module """

from functools import wraps
from typing import Callable

import redis
import requests
from requests import Response

_redis = redis.Redis()
_redis.flushdb()


def counter(method: Callable) -> Callable:
    """
    a counter decorator that counts how many times a particular URL was
    accessed. The value is cached in Redis and will expire after 10 seconds
    """

    @wraps(method)
    def wrapper(url):
        """
        wrapper function
        """
        _redis.incr(f"count:{url}")

        html = _redis.get(f"cached:{url}")
        if html is not None:
            return html.decode("utf-8")
        html = method(url)
        _redis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@counter
def get_page(url: str) -> str:
<<<<<<< HEAD
    """
    a function that returns the HTML content of a particular URL
    """
    response: Response = requests.get(url)
    return response.text
=======
    """ track how many times a particular URL was accessed in the key
        "count:{url}"
        and cache the result with an expiration time of 10 seconds """
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
>>>>>>> 3ea0122c74f157a9e1dd9908bf6ab261a217e83f
