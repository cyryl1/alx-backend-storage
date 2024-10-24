#!/usr/bin/env python3
"""
Module for implementing a Redis cache class
"""
import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class for storing data in Redis
    """

    def __init__(self):
        """
        Initialize the cache with a redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in redis using a random key and return the key
        Args:
            data: The data to store (can be str, bytes, int, or float)
        Returns:
            str: The randomly generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get data from Redis and convert it to the desired format
        Args:
            key: The key to look up in Redis
            fn: Optional callable to convert the retrieve data
        Returns:
            The data in the desired format, or None if the key doesn't exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Get a string value from Redis
        Args:
            key: The key to look up in Redis
        Returns:
            The decoded string value, or None if they doesn't exist
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Get an integer value from Redis
        Args:
            key: The key to look up in Redis
        Returns:
            The integer value, or None if the key doesn't exist
        """
        return self.get(key, fn=int)
