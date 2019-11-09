import pymongo
import dns
from typing import Dict


class Database(object):
    URI = "mongodb://127.0.0.1:27017/pricing"
    # URI = "mongodb+srv://damanbhola:admin@pscluster-tko78.mongodb.net/test?retryWrites=true&w=majority"
    # mongo "mongodb+srv://pscluster-tko78.mongodb.net/test"  --username damanbhola
    DATABASE = pymongo.MongoClient(URI).get_database("pricing")

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)