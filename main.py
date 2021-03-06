from typing import Union, NewType
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
    price: float  null(None): False
    tax: float | None = None  null(None): True
"""

TOKEN_CODE = NewType("TOKEN_CODE", str)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    id: int
    name = "cs lee"
    # name: str = "cs lee"  str 표시의 유무
    signup_ts: datetime | None = None  # 3.10 Version Not Union
    # signup_same: Union[datetime, None] = None  # 3.8, 9 Version
    friends: list[int] = []  # [int, str] str 은 기본 내장


class ReqToken(BaseModel):
    code: str
    number: int
    token_code: TOKEN_CODE | None = None


external_date = {
    "id": "1004",
    "signup_ts": "2022-06-24 12:00",
    "friends": [1, "2", b"3"]
}


user = User(**external_date)


@app.post("/tokens")
def create_token(token: ReqToken):
    return {
        "code": token.code,
        "number": token.number,
        "token_code": token.token_code
    }


@app.post("/new_type_tokens")
def new_type_token(token: ReqToken):
    return f"{token}"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):  # null(None)=true
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

