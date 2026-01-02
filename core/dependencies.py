import os
from functools import lru_cache
from services.conversation_service import ConversationService
from services.sheets_service import SheetsService

@lru_cache()
def get_conversation_service() -> ConversationService:
    return ConversationService(sheets_service=get_sheets_service())

@lru_cache()
def get_sheets_service() -> SheetsService:
    # Read environment variables
    credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
    sheet_id = os.getenv('GOOGLE_SHEET_ID')

    return SheetsService(credentials_path=credentials_path, sheet_id=sheet_id)
