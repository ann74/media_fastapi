from typing import Union

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.config import DB_URL, DB_MODELS
from src.files.router import router as file_router

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

app.include_router(file_router)
