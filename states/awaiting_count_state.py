from typing import Tuple
from domain.models import Guest
from domain.enums import ConversationState
from states.awaiting_dietary_state import AwaitingDietaryState
from states.base_state import BaseState

class AwaitingCountState(BaseState):
    def get_state_name(self) -> ConversationState:
        return ConversationState.AWAITING_COUNT

    def handle_message(self, guest: Guest, message: str) -> Tuple[str, 'BaseState']:
        message_clean = message.strip()

        try:
            guest_count = int(message_clean)

            if guest_count < 1 or guest_count > 10:
                response = "המספר נראה לא סביר. אנא כתוב מספר בין 1 ל-10"
                next_state = self
                return (response, next_state)

            guest.guest_count = guest_count
            response = """קיבלתי ✔️
            יש העדפות תזונה מיוחדות?
            (צמחוני/טבעוני/אלרגיות/אחר)"""
            next_state = AwaitingDietaryState()
            return (response, next_state)
        except ValueError:
            response = "לא הצלחתי להבין. אנא כתוב מספר (לדוגמה: 2)"
            next_state = self
            return (response, next_state)