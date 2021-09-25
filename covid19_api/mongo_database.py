import configparser

from motor.motor_asyncio import AsyncIOMotorClient as Client

# Read config file
config = configparser.RawConfigParser()
config.read('config.ini')

# Get configs
database = config['DEFAULT']['database']
collection_country = config['DEFAULT']['collection_country']
collection_article = config['DEFAULT']['collection_article']
connection_string = config['DEFAULT']['connection_string']


class MongoDatabase:
    """
    MongoDB
    """

    def __init__(self):
        self.__client = Client(connection_string)
        self.__database = self.__client[database]
        self.__collection_country = self.__database[collection_country]
        self.__collection_article = self.__database[collection_article]

    async def get_country(self, name):
        """ Return a country """

        return await self.__collection_country.find_one({'name': name})

    def get_all_countries(self):
        """ Return all countries """

        return self.__collection_country.find()

    def get_all_articles(self):
        """ Return all articles """

        return self.__collection_article.find()
