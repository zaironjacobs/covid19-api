import configparser

import uvicorn

# Read config file
config = configparser.RawConfigParser()
config.read('config.ini')

# Get configs
host = config['DEFAULT']['host']
port = int(config['DEFAULT']['port'])

if __name__ == '__main__':
    uvicorn.run('covid19_api.app:app', host=host, port=port)
