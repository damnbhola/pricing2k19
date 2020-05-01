import pymongo
import dns
import os
from typing import Dict


class Database(object):
    URI = os.environ.get("MONGOLAB_URI")
    print(os.environ.get("MONGOLAB_URI"), os.environ.get("DB"))
    client = pymongo.MongoClient(URI)
    DATABASE = client.get_database(os.environ.get("DB"))

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update_one(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove_one(query)
