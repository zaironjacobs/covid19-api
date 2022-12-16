import configparser

import uvicorn

config = configparser.RawConfigParser()
config.read("config.ini")

if __name__ == "__main__":
    host = config["DEFAULT"]["host"]
    port = int(config["DEFAULT"]["port"])
    uvicorn.run("covid19_api.app:app", host=host, port=port)
