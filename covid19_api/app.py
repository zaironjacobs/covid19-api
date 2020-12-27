from fastapi import FastAPI

from .mongo_database import MongoDatabase
from .country_helper import parse_country

app = FastAPI()
mongo_database = MongoDatabase()


@app.get('/country/', tags=["country"])
async def get_country(name: str):
    country = await mongo_database.get_country(name)
    return parse_country(country)


@app.get('/countries/', tags=["country"])
async def get_countries():
    results = []
    countries = mongo_database.get_all_countries()
    async for country in countries:
        results.append(parse_country(country))
    return results
