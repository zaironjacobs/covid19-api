import uvicorn
from fastapi import FastAPI
from decouple import config

from mongodb import MongoDB

app = FastAPI()
mongo = MongoDB()


@app.get('/')
def index():
    return {'key': 'value'}


@app.get('/country')
def get_country(name: str):
    country = mongo.get_country(name)
    country = {
        'name': country.get('name'),
        'confirmed': country.get('confirmed'),
        'deaths': country.get('deaths'),
        'active': country.get('active'),
        'recovered': country.get('recovered'),
        'last_updated_by_source_at': country.get('last_updated_by_source_at')
    }
    return country


@app.get('/countries')
def get_countries():
    results = []
    countries = mongo.get_all_countries()
    for country in countries:
        results.append({
            'name': country.get('name'),
            'confirmed': country.get('confirmed'),
            'deaths': country.get('deaths'),
            'active': country.get('active'),
            'recovered': country.get('recovered'),
            'last_updated_by_source_at': country.get('last_updated_by_source_at')
        })
    return results


if __name__ == '__main__':
    uvicorn.run('app:app', host=config('HOST'), port=int(config('PORT')), reload=True)
