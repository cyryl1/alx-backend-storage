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
