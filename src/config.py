import os
from dotenv import load_dotenv


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_MODELS = [
    "src.models",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": DB_MODELS,
            "default_connection": "default",
        },
    },
}
