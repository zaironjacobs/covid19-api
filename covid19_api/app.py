from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .models import Article
from .models import Country
from .mongo_db import MongoDatabase

app = FastAPI(docs_url=None, redoc_url="/documentation", title="COVID19 API")
mongo_database = MongoDatabase()


@app.get("/", status_code=200, include_in_schema=False)
def index():
    """Index"""

    return JSONResponse(content={"message": "Covid-19 API"})


@app.get("/countries/{country_name}", status_code=200, tags=["country"])
async def get_country(country_name: str):
    """Get country"""

    country = await mongo_database.get_country(country_name)
    if country:
        country = Country(
            name=country.get("name"),
            confirmed=country.get("confirmed"),
            deaths=country.get("deaths"),
            last_updated_by_source_at=country.get("last_updated_by_source_at"),
        )
        return country.dict()
    else:
        return JSONResponse(status_code=404, content={"detail": "Country not found"})


@app.get("/countries", status_code=200, tags=["country"])
async def get_countries():
    """Get countries"""

    results = []
    countries = mongo_database.get_all_countries()
    async for country in countries:
        country = Country(
            name=country.get("name"),
            confirmed=country.get("confirmed"),
            deaths=country.get("deaths"),
            last_updated_by_source_at=country.get("last_updated_by_source_at"),
        )
        results.append(country.dict())
    if not results:
        return JSONResponse(status_code=404, content={"detail": "Countries not found"})
    return results


@app.get("/articles", status_code=200, tags=["article"])
async def get_articles():
    """Get articles"""

    results = []
    articles = mongo_database.get_all_articles()
    async for article in articles:
        article = Article(
            title=article.get("title"),
            source_name=article.get("source_name"),
            author=article.get("author"),
            description=article.get("description"),
            url=article.get("url"),
            published_at=article.get("published_at"),
        )
        results.append(article.dict())
    if not results:
        return JSONResponse(status_code=404, content={"detail": "Articles not found"})
    return results
