import uvicorn
from decouple import config

if __name__ == '__main__':
    uvicorn.run('covid19_api.app:app', host=config('HOST'), port=int(config('PORT')))
