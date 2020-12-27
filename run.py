import uvicorn
from decouple import config

uvicorn.run('covid19_api.app:app', host=config('HOST'), port=int(config('PORT')))
