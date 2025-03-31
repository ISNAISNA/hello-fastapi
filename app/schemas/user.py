from pydantic import BaseModel, constr

class UserCreate(BaseModel):
    name: constr(min_length=2, max_length=10)