from abc import ABC, abstractmethod
from typing import Tuple
from domain.models import Guest
from domain.enums import ConversationState

class BaseState(ABC):
    """
    Abstract base class defining the contract for all conversation states.
    Each state handles user input and determines the next state transition.
    """

    @abstractmethod
    def handle_message(self, guest: Guest, message: str) -> Tuple[str, 'BaseState']:
        """
        Process user's message and transition to next state.

        Args:
            guest: The Guest object being updated
            message: User's WhatsApp message

        Returns:
            Tuple of (response_message, next_state)
        """
        pass

    @abstractmethod
    def get_state_name(self) -> ConversationState:
        """
        Returns the enum value this state represents.
        """
        pass