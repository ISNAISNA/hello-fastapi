from sqlalchemy.orm import Session, joinedload
from domain.user import User
from schemas.user import UserCreate

def create_user(db_gen: Session, user_in: UserCreate) -> User:
    db_user = User(
        name=user_in.name
    )

    db = next(db_gen)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db_gen:Session, id: int) -> User:
    db = next(db_gen)
    user = db.query(User).options(joinedload(User.items)).filter(User.id==id).first()
    return {"id": user.id, "name":user.name, "items": [{"id": item.id, "name": item.name} for item in user.items]}

def get_users(db_gen:Session, skip: int = 0, limit: int = 10) -> list[User]:
    db = next(db_gen)
    return db.query(User).offset(skip).limit(limit).all()