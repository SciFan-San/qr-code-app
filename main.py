import segno
from io import BytesIO
from typing import Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse


# Instantiate FastAPI server
app = FastAPI()


# Define data Structure for QR Codes
class WifiRequest(BaseModel):
    ssid: str
    password: str
    security_type: str = "WPA"
    hidden: bool = False
    correction_level: str = Field(default="L", pattern="^[LMQHlmqh]$")
    file_name: Optional[str] = "qr_code"


# API GET request logic, parses according to QR type
@app.post("/qr/generate")
async def generate_qr(user_json: WifiRequest, scale: int = 10):
    try:
        wifi_qr_string = f"""
        WIFI:S:{user_json.ssid};
        T:{user_json.security_type};
        P:{user_json.password};
        H:{user_json.hidden};;
        """

        qr_image = segno.make_qr(wifi_qr_string, error=user_json.correction_level)  # type: ignore

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
