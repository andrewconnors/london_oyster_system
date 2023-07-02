from dataclasses import dataclass

from storage.location import Location
from src.constants import TransitType

@dataclass
class Trip:
    fare: float = 0.0
    startStation: Location = None
    endStation: Location = None
    transitType: TransitType = None