from fastapi import APIRouter
from db.database import get_db
from repository.item import create_item as CreateItem, get_items as GetItems
from schemas.item import ItemCreate

router = APIRouter()

@router.get("/items")
def read_item():
    return GetItems(get_db())

@router.post("/items")
def create_item(item: ItemCreate):
    return CreateItem(get_db(), item)  # DB 저장 함수