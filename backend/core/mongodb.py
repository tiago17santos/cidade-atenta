
from functools import lru_cache

from django.conf import settings
from pymongo import MongoClient


@lru_cache(maxsize=1)
def get_mongo_client():
    return MongoClient(
        settings.MONGODB_URI,
        serverSelectionTimeoutMS=5000
    )


def get_database():
    client = get_mongo_client()
    return client[settings.MONGODB_DATABASE]
