from fastapi import FastAPI, HTTPException

from .mongo_database import MongoDatabase
from .country_helper import parse_country
from .article_helper import parse_article

app = FastAPI()
mongo_database = MongoDatabase()


@app.get('/country', tags=['country'])
async def get_country(name: str):
    country = await mongo_database.get_country(name)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return parse_country(country)


@app.get('/countries', tags=['country'])
async def get_countries():
    results = []
    countries = mongo_database.get_all_countries()
    async for country in countries:
        results.append(parse_country(country))
    if not results:
        raise HTTPException(status_code=404, detail="Countries not found")
    return results


@app.get('/articles', tags=['articles'])
async def get_articles():
    results = []
    all_articles = mongo_database.get_all_articles()
    async for article in all_articles:
        results.append(parse_article(article))
    if not results:
        raise HTTPException(status_code=404, detail="Articles not found")
    return results
