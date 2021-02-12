from fastapi import FastAPI, HTTPException

from .mongo_database import MongoDatabase
from .country_helper import parse_country
from .news_helper import parse_news

app = FastAPI()
mongo_database = MongoDatabase()


@app.get('/country/', tags=["country"])
async def get_country(name: str):
    country = await mongo_database.get_country(name)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return parse_country(country)


@app.get('/countries/', tags=["country"])
async def get_countries():
    results = []
    countries = mongo_database.get_all_countries()
    async for country in countries:
        results.append(parse_country(country))
    if not results:
        raise HTTPException(status_code=404, detail="Countries not found")
    return results


@app.get('/news/', tags=["news"])
async def get_news():
    results = []
    all_news = mongo_database.get_all_news()
    async for news in all_news:
        results.append(parse_news(news))
    if not results:
        raise HTTPException(status_code=404, detail="News not found")
    return results
