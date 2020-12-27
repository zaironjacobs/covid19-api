from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient as Client


class MongoDatabase:
    """
    MongoDB
    """

    def __init__(self):
        self.__client = Client((config('CONNECTION_STRING')))
        self.__database = self.__client[config('DATABASE')]
        self.__collection = self.__database[config('COLLECTION')]

    async def get_country(self, name):
        """ Return a country """

        return await self.__collection.find_one({'name': name})

    def get_all_countries(self):
        """ Return all countries """

        return self.__collection.find()
