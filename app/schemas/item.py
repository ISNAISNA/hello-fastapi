from pydantic import BaseModel, constr

class ItemCreate(BaseModel):
    user_id: int
    title: constr(min_length=2, max_length=15)
    description: constr(min_length=2, max_length=15)