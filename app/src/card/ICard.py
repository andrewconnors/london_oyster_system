from typing import Optional

from src.trip.Trip import Trip

class ICard:
    def load(self, amount: float) -> bool:
        raise NotImplementedError("Card.load not implemented")
    
    def balance(self) -> float:
        raise NotImplementedError("Card.balance not implemented")

    def charge(self, amount: float) -> bool:
        raise NotImplementedError("Card.charge not implemented")

    def setCurrentTrip(self, trip: Trip) -> None:
        raise NotImplementedError("Card.setCurrentTrip not implemented")

    def getCurrentTrip(self) -> Optional[Trip]:
        raise NotImplementedError("Card.getCurrentTrip not implemented")

