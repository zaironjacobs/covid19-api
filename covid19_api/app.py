from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response

from .mongo_database import MongoDatabase
from .models import Country
from .models import Article

app = FastAPI(docs_url=None, redoc_url='/documentation', title='COVID19 API')
mongo_database = MongoDatabase()


@app.get('/', status_code=200, include_in_schema=False)
def index():
    """ Index empty """

    return Response(status_code=200)


@app.get('/countries', status_code=200, tags=['country'])
async def get_countries(name: str = None):
    """ Get countries """

    if name:
        country = await mongo_database.get_country(name)
        if country:
            country = Country(name=country.get('name'),
                              confirmed=country.get('confirmed'),
                              deaths=country.get('deaths'),
                              active=country.get('active'),
                              recovered=country.get('recovered'),
                              last_updated_by_source_at=country.get('last_updated_by_source_at'))
            return country.dict()
        else:
            return JSONResponse(status_code=404, content={'detail': 'Country not found'})
    else:
        results = []
        countries = mongo_database.get_all_countries()
        async for country in countries:
            country = Country(name=country.get('name'),
                              confirmed=country.get('confirmed'),
                              deaths=country.get('deaths'),
                              active=country.get('active'),
                              recovered=country.get('recovered'),
                              last_updated_by_source_at=country.get('last_updated_by_source_at'))
            results.append(country.dict())
        if not results:
            return JSONResponse(status_code=404, content={'detail': 'Countries not found'})
        return results


@app.get('/articles', status_code=200, tags=['article'])
async def get_articles():
    """ Get articles """

    results = []
    articles = mongo_database.get_all_articles()
    async for article in articles:
        article = Article(title=article.get('title'),
                          source_name=article.get('source_name'),
                          author=article.get('author'),
                          description=article.get('description'),
                          url=article.get('url'),
                          published_at=article.get('published_at'))
        results.append(article.dict())
    if not results:
        return JSONResponse(status_code=404, content={'detail': 'Articles not found'})
    return results
