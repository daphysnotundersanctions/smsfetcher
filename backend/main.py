from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from db import insert

class Item(BaseModel):
    value : int
    fromWho : str

app = FastAPI()

@app.get("/")
def getCodesList():
    return {"Hello": "World"}


@app.post("/sendMessage/")
async def postMessage(item : Item):
    return insert(item)