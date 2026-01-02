import os
from datetime import datetime
from typing import Optional

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',  # Read/write sheets
    'https://www.googleapis.com/auth/drive'  # Access Drive files
]

class SheetsService:
    def __init__(self, credentials_path: str, sheet_id: str):
        if not os.path.exists(credentials_path):
            raise FileNotFoundError(f"Credentials not found: {credentials_path}")
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(sheet_id)
        self.worksheet = spreadsheet.sheet1  # Use the first sheet

    def get_guest_name(self, phone_number: str) -> Optional[str]:
        """Find guest name by phone number in the spreadsheet."""
        records = self.worksheet.get_all_records()

        for record in records:
            if str(record.get('Phone Number')) == str(phone_number):
                return record.get('Name')

        return None

    def update_rsvp(self, guest_data: dict) -> None:
        """Update existing guest row in spreadsheet."""
        phone_number = guest_data['phone_number']
        is_attending = guest_data['is_attending']
        guest_count = guest_data['guest_count']
        dietary = guest_data['dietary_preferences']
        timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")

        try:
            cell = self.worksheet.find(phone_number)
            row_number = cell.row

            # Update columns C-F (Attending, Count, Dietary, Timestamp)
            values = [[is_attending, guest_count, dietary, timestamp]]
            self.worksheet.update(f'C{row_number}:F{row_number}', values)

            print(f"✅ Updated RSVP for {phone_number} in row {row_number}")
        except Exception as e:
            print(f"❌ Failed to update RSVP for {phone_number}: {e}")
