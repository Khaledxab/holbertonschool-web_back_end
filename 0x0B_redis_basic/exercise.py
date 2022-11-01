#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function."""
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        """Wrapper"""
        self._redis.rpush(inputs, str(args))
        output = method(self, *args)
        self._redis.rpush(outputs, output)
        return output
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Get data from Redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get string from Redis"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Get int from Redis"""
        return self.get(key, int)

def replay(self):
    """Display the history of calls of a particular function"""
    fn_name = self.store.__qualname__
    inputs = self._redis.lrange(fn_name + ":inputs", 0, -1)
    outputs = self._redis.lrange(fn_name + ":outputs", 0, -1)
    print("{} was called {} times:".format(fn_name, self._redis.get(fn_name)))
    for i in range(len(inputs)):
        print("{}(*{}) -> {}".format(fn_name, inputs[i].decode("utf-8"), outputs[i].decode("utf-8")))
