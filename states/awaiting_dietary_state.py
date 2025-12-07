from typing import Tuple
from domain.models import Guest
from domain.enums import ConversationState
from states.base_state import BaseState
from states.completed_state import CompletedState

class AwaitingDietaryState(BaseState):
    def get_state_name(self) -> ConversationState:
        return ConversationState.AWAITING_DIETARY

    def handle_message(self, guest: Guest, message: str) -> Tuple[str, 'BaseState']:
        message_clean = message.strip()
        guest.dietary_preferences = message_clean
        response = "תודה! שמרנו את הפרטים. נתראה בחתונה! 🎉️"
        next_state = CompletedState()
        return (response, next_state)