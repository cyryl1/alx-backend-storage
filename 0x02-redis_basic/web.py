import requests
import time
from functools import wraps
from typing import Dict, Any, Callable

cache: Dict[str, Any] = {}
request_counts: Dict[str, int] = {}

def cache_with_expiry(expiration_seconds: int = 10) -> Callable:
    """
    Decorator that caches function results with expiration time and tracks request counts.

    Args:
        expiration_seconds (int); Number of seconds before cache expired
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str, *args, **kwargs) -> str:
            current_time = time.time()
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"

            request_counts[count_key] = request_counts.get(count_key, 0) + 1

            if cache_key in cache:
                cache_result, timestamp = cache[cache_key]
                if current_time - timestamp < expiration_seconds:
                    return cached_result

            result = func(url, *args, **kwargs)
            cache[cache_key] = (result, current_time)
            return result

        return wrapper
    return decorator

@cache_with_expiry(10)
def get_page(url str) -> str:
    """
    Fetches HTML content from a URL with caching and request counting.

    Args:
        url (str): The URL to fetch

    Returnd:
        str: The HTML content of the page
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def get_request_count(url: str) -> int:
    """
    Get the number of times a URL has been requested.

    Args:
        url (str): The URL to check

    Returns:
        int: Number of times the URL has been requested
    """
    return requested_counts.get(f"count:{url}", 0)
