import os
import sys
from dotenv import load_dotenv
from twilio.rest import Client

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Now we can import from services
from services.sheets_service import SheetsService

# Load environment variables
load_dotenv()


def send_personalized_whatsapp(phone_number: str):
    """
    Send a personalized WhatsApp message using template with name from Google Sheets.

    Args:
        phone_number: Phone number in format '972XXXXXXXXX' (without +)
    """
    # Get Twilio credentials
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_whatsapp = os.getenv('TWILIO_WHATSAPP_NUMBER')
    content_sid = os.getenv('TWILIO_CONTENT_SID')

    # Get Google Sheets credentials
    creds_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
    sheet_id = os.getenv('GOOGLE_SHEET_ID')

    print(f"📋 Looking up phone number: {phone_number}")

    # Create sheets service and look up name
    try:
        sheets_service = SheetsService(creds_path, sheet_id)
        guest_name = sheets_service.get_guest_name(phone_number)
    except Exception as e:
        print(f"❌ Error connecting to Google Sheets: {e}")
        return

    # Check if name was found
    if not guest_name:
        print(f"❌ Phone number {phone_number} not found in Google Sheets!")
        print("Please add this number to your sheet with Name and Phone Number columns.")
        return

    print(f"✅ Found name: {guest_name}")

    # Prepare WhatsApp format
    to_whatsapp = f'whatsapp:+{phone_number}'

    print(f"📱 Sending WhatsApp message to {guest_name} ({to_whatsapp})")

    # Send message with name variable
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            content_sid=content_sid,
            from_=from_whatsapp,
            to=to_whatsapp,
            content_variables=f'{{"1":"{guest_name}"}}'  # {{1}} = guest name
        )

        print(f"✅ Message sent successfully!")
        print(f"Message SID: {message.sid}")
        print(f"Status: {message.status}")
        print(f"Sent to: {guest_name} at {to_whatsapp}")

    except Exception as e:
        print(f"❌ Error sending message: {e}")


if __name__ == "__main__":
    # Test with your friend's number
    # REPLACE THIS with your friend's actual phone number!
    friend_phone = "972543170570"  # Format: 972XXXXXXXXX (no + or spaces)

    print("🤖 Wedding RSVP Bot - WhatsApp Test")
    print("=" * 50)

    send_personalized_whatsapp(friend_phone)

    print("=" * 50)
    print("Done!")

