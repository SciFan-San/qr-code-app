import segno
import json
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()


@app.get("/qr/{user_json}")
async def home(user_json: str, scale: int = 10):
    user_qr_info = json.loads(user_json)  # type: ignore

    qr_image = segno.make_qr(
        f"""WIFI:
        S:{user_qr_info["ssid"]};
        T:{user_qr_info["security_type"]};
        P:{user_qr_info["password"]};
        H:{user_qr_info["hidden"]};;
        """,
        error=user_qr_info["correction_level"]
    )

    qr_image_buffer = BytesIO()
    qr_image.save(qr_image_buffer, kind="PNG", scale=scale)
    qr_image_buffer.seek(0)

    return StreamingResponse(content=qr_image_buffer, media_type="img/png")
