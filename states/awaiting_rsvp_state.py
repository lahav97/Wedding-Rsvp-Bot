from typing import Tuple
from domain.models import Guest
from domain.enums import ConversationState
from states.base_state import BaseState
from states.awaiting_count_state import AwaitingCountState
from states.completed_state import CompletedState

class AwaitingRsvpState(BaseState):
    def get_state_name(self) -> ConversationState:
        return ConversationState.AWAITING_RSVP

    def handle_message(self, guest: Guest, message: str) -> Tuple[str, 'BaseState']:
        message = message.strip().lower()

        if "כן" in message:
            guest.is_attending = True
            response = f"איזה כיף {guest.guest_name}! 🙌\n\nכמה אנשים מגיעים?"
            next_state = AwaitingCountState()
            return (response, next_state)
        elif "לא" in message:
            guest.is_attending = False
            response = "תודה שעדכנת, נשמח לראות אתכם בהזדמנות הבאה !"
            next_state = CompletedState()
            return (response, next_state)
        else:
            # Don't update guest - message is unclear
            response = "לא הצלחתי להבין, אנא ענה 'כן' או 'לא'"
            next_state = self
            return (response, next_state)
