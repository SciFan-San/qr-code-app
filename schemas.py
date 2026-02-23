from typing import Optional, Literal
from pydantic import BaseModel, Field, HttpUrl, ValidationError, field_validator


# Define data Structure for all QR Code types
class WifiRequest(BaseModel):
    qr_type: Literal['wifi']
    ssid: str
    password: str
    security_type: str = "WPA"
    hidden: bool = False
    correction_level: str = Field(default="L", pattern="^[LMQHlmqh]$")
    file_name: Optional[str] = "qr_code"


class UrlRequest(BaseModel):
    qr_type: Literal['url']
    url: HttpUrl

    @field_validator('url')
    @classmethod
    def check_url_safety(cls, link: HttpUrl) -> HttpUrl:
        if link.scheme != 'https':
            raise ValidationError("URL must use https")
        return link


class Binary_Byte(BaseModel):
    qr_type: Literal['binary', 'byte']
    pass


class Kanji_Kana(BaseModel):
    qr_type: Literal['kanji', 'kana']
    pass
