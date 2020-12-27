COVID-19 API
=================
API built with FastAPI.

Works with:

- [COVID-19 Data Fetcher - Python](https://github.com/zaironjacobs/covid19-data-fetcher-python)

- [COVID-19 Data Fetcher - PHP](https://github.com/zaironjacobs/covid19-data-fetcher-php)

- [COVID-19 Data Fetcher - JavaScript](https://github.com/zaironjacobs/covid19-data-fetcher-javascript)

### Download
```
$ git clone https://github.com/zaironjacobs/covid19-api-fastapi
```

### Usage
Copy the file .env.example to .env and fill in the environment variables, then the steps below:
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