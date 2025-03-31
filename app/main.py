from fastapi import FastAPI
from api.v1.endpoints import item, user
from db.database import engine, Base

app = FastAPI()

try:
    with engine.connect() as connection:
        print("Database connected successfully")
except Exception as e:
    print(f"Connection failed: {e}")

Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(item.router)
