from typing import Dict
from domain.models import Guest
from states.base_state import BaseState
from states.awaiting_rsvp_state import AwaitingRsvpState

class ConversationService:
    """
    Manages guest state and routes messages to appropriate state handlers.
    """

    def __init__(self, sheets_service):
        # Dictionary mapping phone_number -> Guest object
        self.guests: Dict[str, Guest] = {}

        # Dictionary mapping phone_number -> current State object
        self.states: Dict[str, BaseState] = {}

        # Service for saving completed RSVPs
        self.sheets_service = sheets_service

    def process_message(self, phone_number: str, message: str) -> str:
        guest = self._get_or_create_guest(phone_number)
        current_state = self._get_or_create_state(phone_number)
        response, next_state = current_state.handle_message(guest, message)
        self.states[phone_number] = next_state

        if guest.is_complete():
            self._save_to_sheets(guest)

        return response

    def _get_or_create_guest(self, phone_number: str) -> Guest:
        if phone_number not in self.guests:
            self.guests[phone_number] = Guest(phone_number=phone_number)
        return self.guests[phone_number]

    def _get_or_create_state(self, phone_number: str) -> BaseState:
        if phone_number not in self.states:
            self.states[phone_number] = AwaitingRsvpState()
        return_state = self.states[phone_number]

    def _save_to_sheets(self, guest: Guest) -> None:
        """Save completed RSVP to Google Sheets."""
        self.sheets_service.save_sheet(guest.to_dict())
