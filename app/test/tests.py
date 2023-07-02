from typing import Dict

import unittest

from src.card.MockCard import MockCard
from src.constants import TransitType
from src.terminal.Terminal import Terminal
from storage.location import Location

class LondonOysterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.terminal = Terminal()
        self.card = MockCard()

    def test_load(self) -> None:
        self.assertEqual(self.card.balance(), 0)
        self.card.load(25)
        self.assertEqual(self.card.balance(), 25)

    def test_bus_trip(self) -> None:
        self.card.load(25)
        self.assertEqual(self.card.balance(), 25)
        self.terminal.tapIn(self.card, TransitType.BUS, Location("Earl's Court", [1,2]))
        expectedBalance = 25 - 1.8
        self.assertEqual(self.card.balance(), expectedBalance)

        # Make sure a tap out is a no-op on bus routes
        self.assertEqual(self.terminal.tapOut(self.card, TransitType.BUS, Location("Holmberg", [1,2])), False)
        self.assertEqual(self.card.balance(), expectedBalance)
    
    def test_no_tap_out(self) -> None:
        self.card.load(25)
        self.terminal.tapIn(self.card, TransitType.TUBE, Location("Earl's Court", [1,2]))
        # Ensure no charge yet
        self.assertEqual(self.card.balance(), 25)
        self.terminal.tapIn(self.card, TransitType.TUBE, Location("Earl's Court", [1,2]))
        # Assert we were charged the max fare
        self.assertEqual(self.card.balance(), 25 - 3.20)
    
    def test_customer_friendly(self) -> None:
        # Test that we give the customer the best rate on trips where > 1 rate is possible
        self.card.load(25)
        self.terminal.tapIn(self.card, TransitType.TUBE, Location("Holburn", [1]))
        self.terminal.tapOut(self.card, TransitType.TUBE, Location("Earl's Court", [1,2]))
        
        expectedBalance = 25 - 2.50 # Zone 1 to 1 charge, not 1 to 2.
        self.assertEqual(self.card.balance(), expectedBalance)
    
    def test_example_trip(self) -> None:
        # Test out a more complex trip
        self.card.load(30)

        # Holburn -> Earl's Court (Tube)
        self.terminal.tapIn(self.card, TransitType.TUBE, Location("Holburn", [1]))
        self.terminal.tapOut(self.card, TransitType.TUBE, Location("Earl's Court", [1,2]))

        # Earl's Court -> Chelsea (Bus)
        self.terminal.tapIn(self.card, TransitType.BUS, Location("Earl's Court", [1]))

        # Chelsea -> Wimbledon (Tube)
        self.terminal.tapIn(self.card, TransitType.TUBE, Location("Chelsea", [1]))
        self.terminal.tapOut(self.card, TransitType.TUBE, Location("Wimbledon", [3]))


