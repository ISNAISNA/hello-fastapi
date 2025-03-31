from fastapi import APIRouter
from db.database import get_db
from repository.user import create_user as CreateUser, get_users as GetUsers, get_user as GetUser
from schemas.user import UserCreate

router = APIRouter()

@router.get("/users")
def read_users():
    return GetUsers(get_db())

@router.get("/users/{id}")
def read_user(id: int):
    return GetUser(get_db(), id)

@router.post("/users")
def create_user(user: UserCreate):
    return CreateUser(get_db(), user)

