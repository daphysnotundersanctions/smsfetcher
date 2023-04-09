from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    value : str

app = FastAPI()

@app.get("/")
def getCodesList():
    return {"Hello": "World"}


@app.post("/sendMessage/")
async def postMessage(item : Item):
    return item