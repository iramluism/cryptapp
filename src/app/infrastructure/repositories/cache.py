from typing import Dict

import redis
from simple_settings import settings


class Cache:
    def __init__(self) -> None:
        self._db_name = settings.REDIS_CACHE_DB
        self._host = settings.REDIS_SERVER_HOST
        self._port = settings.REDIS_SERVER_PORT

        self._redis_cli = redis.Redis(
            host=self._host, port=self._port, db=self._db_name
        )

        self.ping()

    def ping(self):
        return self._redis_cli.ping()

    def save_map(self, key, data: Dict[str, str]):
        self._redis_cli.hset(key, mapping=data)

    def add_to_set(self, key, value):
        self._redis_cli.sadd(key, value)

    def get_set(self, key):
        return self._redis_cli.smembers(key)

    def get_map_value(self, key, fields):
        return self._redis_cli.hmget(key, fields)
