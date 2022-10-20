from fastapi import FastAPI, Body, BackgroundTasks
from search import helper_on_search

app = FastAPI()


def on_search_callback(data: dict):
    print('on search callback called')
    helper_on_search(data)


@app.post("/v1/search")
async def read_root(background_tasks: BackgroundTasks, data: dict = Body()) -> dict:
    background_tasks.add_task(on_search_callback, data)
    resp = {
        "message": {
            "ack": {
                "status": "ACK"
            }
        }
    }
    return resp
