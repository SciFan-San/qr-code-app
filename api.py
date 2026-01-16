from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def home(user_string: str):
    return {"message": "QR String Received!"}
