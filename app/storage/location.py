from typing import List
from dataclasses import dataclass

@dataclass
class Location:
    name: str
    zones: List[int]