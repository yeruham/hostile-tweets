from fastapi import FastAPI
import uvicorn
import os
from manager import Manager


USER = os.getenv("USER", "IRGC")
PASSWORD = os.getenv("PASSWORD", "iraniraniran")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")
TEXT_KEY = os.getenv("TEXT_KEY", "Text")

app = FastAPI()

app.state.manager = None


def run_manager(user, password, database, collection,  text_key, weapons):
    manager = Manager(user, password, database, collection)
    connect = manager.fetch_data()
    if connect:
        manager.run_processes(text_key, weapons)
        return manager
    else:
        return None


def get_weapons():
    if os.path.exists('../data/weapon_list.txt'):
        path = '../data/weapon_list.txt'
    else:
        path = 'weapon_list.txt'
    with open(path, 'r') as f:
        weapons = f.read().split('\n')
    return weapons


@app.get('/')
async def api_information():
    return {"massage: this api of hostile-tweets, get processed_data in path /processed_data"}



@app.get('/processed_data')
async def get_processed_data():
    if app.state.manager is None:
        weapons = get_weapons()
        app.state.manager = run_manager(USER, PASSWORD, DB, COLLECTION, TEXT_KEY, weapons)

    if app.state.manager is None:
        return {"status: ": "fail to connect"}

    processed_data = app.state.manager.get_processed_data()
    return processed_data




if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0", port=8080)
