from tortoise.contrib.pydantic import pydantic_model_creator

from src.files.schemas import FileSchema
from src.models import File


file_pydantic = pydantic_model_creator(File)


async def create_file(file_item: FileSchema):
    new_file = await File.create(**file_item.dict())
    return new_file.uuid


async def get_files():
    file_list = File.all()
    return await file_pydantic.from_queryset(file_list)


async def get_file(uuid):
    file_item = File.get(uuid=uuid)
    return await file_pydantic.from_queryset_single(file_item)
