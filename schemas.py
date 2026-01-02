from pydantic import BaseModel

class WhatsAppMessage(BaseModel):
    phone_number: str
    message: str