from fastapi import FastAPI, Depends, Form
from fastapi.responses import Response
from core.dependencies import get_conversation_service
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.post("/webhook")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...),
    conversation_service = Depends(get_conversation_service),
):
    raw = From.strip()

    phone_number = (
        raw.replace("whatsapp:", "")
           .replace("+", "")
           .replace(" ", "")
           .strip()
    )

    message = Body.strip()

    # פה אתה משתמש בשירות השיחה שכבר בנית
    reply_text = conversation_service.process_message(phone_number, message)

    # Twilio מצפה ל-TwiML (XML) עם <Message>
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply_text}</Message>
</Response>"""

    return Response(content=twiml, media_type="application/xml")


@app.get("/")
def root():
    return {"message": "Wedding RSVP Bot is in duty!"}
