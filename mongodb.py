from pymongo import MongoClient
from decouple import config


class MongoDB:
    """
    MongoDB
    """

    def __init__(self):
        self.__client = MongoClient(config('CONNECTION_STRING'))
        self.__database = self.__client[config('DATABASE')]
        self.__collection = self.__database[config('COLLECTION')]

    def get_all_countries(self):
        """ Return all countries """

        return self.__collection.find({})

    def get_country(self, name):
        """ Return a country """

        return self.__collection.find_one({'name': name})
