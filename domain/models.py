from dataclasses import dataclass
from typing import Optional

@dataclass
class Guest:
    """
    Domain model representing a wedding guest and their RSVP status.
    """
    phone_number: str
    is_attending: Optional[bool] = None
    guest_count: Optional[int] = None
    dietary_preferences: Optional[str] = None

    # Determines if RSVP data collection is complete.
    def is_complete(self) -> bool:
        # If they haven't answered yet, not complete
        if self.is_attending is None:
            return False

        # If not attending, we're done - don't need count or dietary
        if self.is_attending is False:
            return False

        # If attending, need both count and dietary preferences
        return (
            self.guest_count is not None and
            self.dietary_preferences is not None
        )

    def to_dict(self) -> dict:
        ''' Returns a dict representation of this Guest. '''
        return {
            'phone_number': self.phone_number,
            'is_attending': self.is_attending,
            'guest_count': self.guest_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Guest':
        ''' Returns a Guest from a dict representation. '''
        return cls(
            phone_number=data['phone_number'],
            is_attending=data['is_attending'],
            guest_count=data['guest_count'],
        )