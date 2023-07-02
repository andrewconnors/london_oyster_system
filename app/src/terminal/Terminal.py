from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
import math

from src.card.ICard import ICard
from src.constants import TransitType
from src.trip.Trip import Trip
from storage.location import Location

class Terminal:
    def computeFare(self, trip: Trip) -> float:
        zonesTravelled: Set[int] = self.computeZonesTravelled(trip.startStation.zones, trip.endStation.zones)
        
        if len(zonesTravelled) == 3:
            return 3.20
        elif len(zonesTravelled) == 1:
            if 1 in zonesTravelled:
                return 2.50
            else:
                return 2.00
        else:
            if 1 in zonesTravelled:
                return 3.00
            else:
                return 2.25

    def computeZonesTravelled(self, startZone: List[int], endZone: List[int]) -> Set[int]:
        '''
        Locations can live across more than one zone, if this happens, we shold charge the customer
        the least amount of money. We assume here that zones must be adjacent 
        i.e. a station in zones 1 and 3 is not possible
        
        Based on this assumption, we can walk through the list and try to minimize the difference between 
        any two values across start and end zones.
        
        One thing we need to look out for is a case like start = [1,2] and end = [1,2]. In this case, {1,1} is more expensive than {2,2}
        even though they are both within the same zone. We solve for this by sorting and working backwards through the list. If we hit
        equal numbers, we'll return the ones outside zone 1 first.
        '''
        startZone.sort(reverse=True)
        endZone.sort(reverse=True)
        minSum:float = math.inf
        minPair: Tuple[int, int] = None
        p1: int = 0
        p2: int = 0

        while p1<len(startZone) and p2<len(endZone):
            if(startZone[p1] == endZone[p2]):
                return set([startZone[p1]])
            if abs(startZone[p1] - endZone[p2]) < minSum:
                minSum = abs(startZone[p1] - endZone[p2])
                minPair = (startZone[p1], endZone[p2])
            
            if (startZone[p1] > endZone[p2] and p1 < len(startZone)):
                p1 += 1
            else:
                p2 += 1
        
        return set(list(range(min(minPair), max(minPair) + 1)))

    def tapIn(self, card: ICard, transitType: TransitType, location: Location) -> bool:
        # Handle outstanding trip
        oldTrip: Trip = card.getCurrentTrip()
        if (oldTrip and not card.charge(oldTrip.fare)):
            # Charge max amount after no tap out, 
            # do not allow entrance if balance is too low.
            return False

        newTrip: Trip = Trip()
        if transitType == TransitType.BUS:
            card.charge(1.8)
            # No need to tap out, current trip is none
            card.setCurrentTrip(None)
            return True
        else:
            # Charge the max amount until tap out
            newTrip.fare = 3.20
            newTrip.startStation = location
            newTrip.transitType = transitType
            card.setCurrentTrip(newTrip)
            return True
    

    def tapOut(self, card: ICard, transitType: TransitType, location: Location) -> bool:
        if transitType == TransitType.BUS or not card.getCurrentTrip():
            return False

        card.getCurrentTrip().endStation = location
        card.charge(self.computeFare(card.getCurrentTrip()))
        card.setCurrentTrip(None)
        return True
        

