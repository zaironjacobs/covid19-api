COVID-19 API
=================
COVID-19 API built with [FastAPI](https://github.com/tiangolo/fastapi).

## Dependencies

- [COVID-19 Data Fetcher](https://github.com/zaironjacobs/covid19-data-fetcher)
- [MongoDB](https://www.mongodb.com)

### Install & run

Copy the file config.ini.example to config.ini and fill in the environment variables.

```
pip install -r requirements.txt
python asgi.py
```

### Endpoints

/countries/Netherlands:

```
{
    "name": "Netherlands",
    "confirmed": 764907,
    "deaths": 11062,
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
        "last_updated_by_source_at": "2020-12-27T05:22:55"
    },
    {
        "name": "Albania",
        "confirmed": 55755,
        "deaths": 1143,
        "last_updated_by_source_at": "2020-12-27T05:22:55"
    },
    {
        "name": "Algeria",
        "confirmed": 97857,
        "deaths": 2722,
        "last_updated_by_source_at": "2020-12-27T05:22:55"
    },
    
    .....
]
```

/articles:

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