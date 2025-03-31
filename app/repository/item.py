from sqlalchemy.orm import Session
from domain.item import Item
from schemas.item import ItemCreate

def create_item(db_gen: Session, item_in: ItemCreate) -> Item:
    db_item = Item(
        user_id=item_in.user_id,
        title=item_in.title,
        description=item_in.description
    )

    db = next(db_gen)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

def get_item(db_gen:Session, id: int) -> Item:
    db = next(db_gen)
    return db.query(Item).filter(Item.id==id).first()

def get_items(db_gen:Session, skip: int=0, limit: int=10) -> list[Item]:
    db = next(db_gen)
    return db.query(Item).offset(skip).limit(limit).all()