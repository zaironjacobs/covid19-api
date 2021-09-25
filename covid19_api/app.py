from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response

from .mongo_database import MongoDatabase
from .country_helper import parse_country
from .article_helper import parse_article

app = FastAPI(docs_url=None, redoc_url='/documentation', title='COVID19 API')
mongo_database = MongoDatabase()


@app.get('/', status_code=200, include_in_schema=False)
def index():
    """ Index empty """

    return Response(status_code=200)


@app.get('/country', status_code=200, tags=['country'])
async def get_country(name: str):
    """ Get a country """

    country = await mongo_database.get_country(name)
    if not country:
        return JSONResponse(status_code=404, content={'detail': 'Country not found'})
    return parse_country(country)


@app.get('/countries', status_code=200, tags=['country'])
async def get_countries():
    """ Get all countries """

    results = []
    countries = mongo_database.get_all_countries()
    async for country in countries:
        results.append(parse_country(country))
    if not results:
        return JSONResponse(status_code=404, content={'detail': 'Countries not found'})
    return results


@app.get('/articles', status_code=200, tags=['article'])
async def get_articles():
    """ Get articles """

    results = []
    all_articles = mongo_database.get_all_articles()
    async for article in all_articles:
        results.append(parse_article(article))
    if not results:
        return JSONResponse(status_code=404, content={'detail': 'Articles not found'})
    return results
