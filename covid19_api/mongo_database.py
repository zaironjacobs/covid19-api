from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient as Client


class MongoDatabase:
    """
    MongoDB
    """

    def __init__(self):
        self.__client = Client((config('CONNECTION_STRING')))
        self.__database = self.__client[config('DATABASE')]
        self.__collection_country = self.__database[config('COLLECTION_COUNTRY')]
        self.__collection_article = self.__database[config('COLLECTION_ARTICLE')]

    async def get_country(self, name):
        """ Return a country """

        return await self.__collection_country.find_one({'name': name})

    def get_all_countries(self):
        """ Return all countries """

        return self.__collection_country.find()

    def get_all_articles(self):
        """ Return all articles """

        return self.__collection_article.find()
