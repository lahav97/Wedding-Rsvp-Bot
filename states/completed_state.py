from typing import Tuple
from domain.models import Guest
from domain.enums import ConversationState
from states.base_state import BaseState

class CompletedState(BaseState):
    def get_state_name(self) -> ConversationState:
        return ConversationState.COMPLETED

    def handle_message(self, guest: Guest, message: str) -> Tuple[str, 'BaseState']:
        message_clean = message.strip()

        response = """כבר השלמת את האישור שלך! ✔️
        רוצה לעדכן משהו? 
        צור קשר: להב - 0543170570"""
        next_state = self
        return (response, next_state)