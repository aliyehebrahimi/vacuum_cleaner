# Location: a location within Vacuum World.
# Each location has an id and, possibly, some dirt.
from typing import Union

class Location:

    def __init__(self, id: str, dirt: Union[bool, str, None] = None):
        self.id = id
        self.dirt = dirt

    def apply_suction(self):
        self.dirt = None
