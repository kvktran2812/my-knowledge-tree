from typing import Union

from fastapi import FastAPI

app = FastAPI()


# root route
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/knowledges/{id}")
def read_knowledge(id: int):
    return {
        "id": id,
        "data": "some data"
    }

