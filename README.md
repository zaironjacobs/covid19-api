COVID-19 API
=================
COVID-19 API built with [FastAPI](https://github.com/tiangolo/fastapi).

Works with:

- [COVID-19 Data Fetcher - Python](https://github.com/zaironjacobs/covid19-data-fetcher-python)

- [COVID-19 Data Fetcher - PHP](https://github.com/zaironjacobs/covid19-data-fetcher-php)

- [COVID-19 Data Fetcher - JavaScript](https://github.com/zaironjacobs/covid19-data-fetcher-javascript)

### Download
```
$ git clone https://github.com/zaironjacobs/covid19-api-fastapi
```

### Usage
Copy the file .env.example to .env and fill in the environment variables.
A local connection example:
```
DATABASE=covid19
COLLECTION_COUNTRY=country
COLLECTION_NEWS=news
CONNECTION_STRING=mongodb://localhost:27017
HOST=localhost
PORT=8050
```

To use:
```
$ cd ~/covid19-api-fastapi
$ pipenv install
$ pipenv run python run.py
```

### Endpoints

/country?name=Netherlands:
```
{
    "name": "Netherlands",
    "confirmed": 764907,
    "deaths": 11062,
    "active": 744871,
    "recovered": 8974,
    "last_updated_by_source_at": "2020-12-27T05:22:55"
}
```

/countries:
```
[
    {
        "name": "Afghanistan",
        "confirmed": 50886,
        "deaths": 2149,
        "active": 7953,
        "recovered": 40784,
        "last_updated_by_source_at": "2020-12-27T05:22:55"
    },
    {
        "name": "Albania",
        "confirmed": 55755,
        "deaths": 1143,
        "active": 23431,
        "recovered": 31181,
        "last_updated_by_source_at": "2020-12-27T05:22:55"
    },
    {
        "name": "Algeria",
        "confirmed": 97857,
        "deaths": 2722,
        "active": 29630,
        "recovered": 65505,
        "last_updated_by_source_at": "2020-12-27T05:22:55"
    },
    
    .....
    
]
```

/news:
```
[
    {
    "title": "US CDC says fully vaccinated people need not quarantine after COVID-19 exposure",
    "source_name": "CNA",
    "author": "CNA",
    "description": "WASHINGTON: People who have received the full course of...",
    "url": "https://www.channelnewsasia.com/news/world/covid-19-vaccine-no-quarantine-14-days-exposure-us-cdc-14173034",
    "published_at": "2021-02-11T12:37:14Z"
    },
    {
    "title": "US could have averted 40% of Covid deaths, says panel examining Trump's policies (Amanda Holpuch/The Guardian)",
    "source_name": "Memeorandum.com",
    "author": null,
    "description": "Amanda Holpuch / The Guardian:\nUS could have averted 40% of Covid...",
    "url": "https://www.memeorandum.com/210211/p12",
    "published_at": "2021-02-11T12:35:00Z"
    },
    
    .....
]
```