from fastapi import APIRouter

from src.files.schemas import FileSchema
from src.files.service import create_file, get_files, get_file

router = APIRouter(
    prefix="/api/file",
    tags=["file"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def upload_file(file_item: FileSchema):
    """Загрузка файла и сохранение иформации в БД"""
    file_uuid = await create_file(file_item)
    return {"status": "ok", "uuid": file_uuid}


@router.get("/")
async def get_file_list():
    """Получить список файлов"""
    file_list = await get_files()
    return {"status": "ok", "data": file_list}


@router.get("/{uuid}")
async def get_file_item(uuid: str):
    """Получить файл по uuid"""
    file_item = await get_file(uuid)
    return {"status": "ok", "data": file_item}