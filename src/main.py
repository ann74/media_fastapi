from typing import Union

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.config import DB_URL, DB_MODELS

app = FastAPI()


register_tortoise(
    app,
    config=None,
    config_file=None,
    db_url=DB_URL,
    modules={"models": DB_MODELS},
    generate_schemas=False,
    add_exception_handlers=False
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
