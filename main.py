import segno
import json
from pydantic import BaseModel, Field, WithJsonSchema
from fastapi import FastAPI

app = FastAPI()


class UserInputNoWifi(BaseModel):
    filename: str = Field(default="image")
    encoding_string: str


class UserInputWifi(BaseModel):
    ssid: str
    password: str | None
    security: str | None
    hidden: bool


@app.post("/")
async def home(user_json=str):
    user_qr_info = json.loads(user_json)
    segno.make_qr()


user_json = json.dump()

qr = segno.make(user_json)
qr.save(user_json.name)