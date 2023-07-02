from typing import Optional

from src.card.ICard import ICard
from src.trip.Trip import Trip

class MockCard(ICard):
    def __init__(self) -> None:
        self._balance: float = 0.0
        self._trip: Optional[Trip] = None

    def load(self, amount: float) -> bool:
        if(amount > 0):
            self._balance += amount
            return True
        return False
    
    def balance(self) -> float:
        return self._balance
    
    def charge(self, amount) -> bool:
        if (self._balance < amount):
            return False
        else:
            self._balance -= amount
            return True
    
    def setCurrentTrip(self, trip: Trip) -> None:
        self._trip = trip
    
    def getCurrentTrip(self) -> Optional[Trip]:
        return self._trip

