# State: the vacuum world.
# The state of the world consists of all of the locations in the world,
# and the current location of the vacuum.
from location import Location
from typing import Dict


class State:

    def __init__(self, locations: Dict[str, Location], current_location_id: str):
        self.locations = locations
        self.current_location_id = current_location_id

    def current_location(self) -> Location:
        return self.locations[self.current_location_id]
