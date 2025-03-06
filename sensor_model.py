# SensorModel: a definition of how the current location is reflected in the
# agent percepts. This decouples the ModelReflexVacuum from the actual state of
# the world, and encapsulates how a sensor might be exposed as a percept API.

from state import State


class SensorModel:

    def __init__(self, state: State):
        self.state = state

    def sense_dirt(self) -> bool:
        return self.state.current_location().dirt is not None

    def sense_location_id(self) -> str:
        return self.state.current_location().id
