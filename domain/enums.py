from enum import Enum

class ConversationState(Enum):
    """
    Defines all possible states in the RSVP conversation flow.
    """
    AWAITING_RSVP = "awaiting_rsvp"
    AWAITING_COUNT = "awaiting_count"
    AWAITING_DIETARY = "awaiting_dietary"
    COMPLETED = "completed"
