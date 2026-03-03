import segno
import schemas
from io import BytesIO
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import StreamingResponse
from typing import Union

# Instantiate FastAPI server
app = FastAPI()


# API GET request logic, parses according to QR type
@app.post("/qr/generate")
async def generate_qr(user_json: Union[schemas.WifiRequest, schemas.UrlRequest, schemas.Binary_Byte, schemas.Kanji_Kana] = Body(discriminator="qr_type"), scale: int = 10):
    try:
        qr_string = str
        qr_image = any

        if type(user_json) is schemas.WifiRequest:
            qr_string = f"WIFI:S:{user_json.ssid};T:{user_json.security_type};P:{user_json.password};H:{user_json.hidden};;"
            qr_image = segno.make_qr(qr_string, error=user_json.correction_level)  # type: ignore
        elif type(user_json) is schemas.UrlRequest:
            qr_string = user_json.url
            qr_image = segno.make_qr(str(qr_string))  # type: ignore
        elif type(user_json) is schemas.Binary_Byte:
            qr_string = user_json
        elif type(user_json) is schemas.Kanji_Kana:
            qr_string = user_json

        image_buffer = BytesIO()
        qr_image.save(image_buffer, kind="PNG", scale=scale)
        image_buffer.seek(0)

        return StreamingResponse(
            content=image_buffer,
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename={user_json.file_name}"}
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"QR Generation failed: {str(e)}"
        )
