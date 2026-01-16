from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home(user_string: str):
    return {"message": "QR String Received!"}
