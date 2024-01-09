from fastapi import FastAPI
from typing import List, Optional
from models import User, Gender, Role
from uuid import uuid4


app = FastAPI()

database: List[User] = [
    User(
        id=uuid4(),
        first_name="Gbenga",
        last_name="Ilesanmi",
        middle_name="Samuel",
        gender=Gender.male,
        roles=[Role.student],
    ),
    User(
        id=uuid4(),
        first_name="Daniel",
        last_name="Farrow",
        middle_name="D",
        gender=Gender.male,
        roles=[Role.teacher, Role.student],
    ),
]


@app.get("/")
async def root():
    return {"Hello": "Gbenga"}


@app.get("/fetch/")
async def fetch_users():
    return database


@app.post("/post/")
async def post_user(user: User):
    database.append(user)
    return database

@app.put("/put/")
async def update_user(user: User):
    for i in database:
        if user.first_name != 'null':
            i.first_name = user.first_name

