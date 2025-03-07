# ModelReflexVacuum: A robot vacuum cleaner modeled as a model-based reflex agent.
# Your implementation should pass the tests in test_model_reflex_vacuum.py.
# Aliyeh Ebrahimi

from location import Location
from movement_model import MovementModel
from state import State
from transition_model import TransitionModel
from sensor_model import SensorModel
from typing import Callable


class ModelReflexVacuum:
    """
    A model-based reflex agent for a vacuum cleaner.

    Attributes:
        state (State): The current state of the environment.
        transition_model (TransitionModel): The transition model for environment interaction.
        sensor_model (SensorModel): The sensor model for environment perception.
        most_recent_action (callable): The most recent action performed by the agent.
    """

    def __init__(
        self, state: State, transition_model: TransitionModel, sensor_model: SensorModel
    ):
        self.state = state
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.most_recent_action = None

    def suck(self):
        """Cleans the dirt at the current location."""
        self.transition_model.apply_suction()
        self.most_recent_action = None

    def move_left(self):
        """Moves the agent to the left location."""
        self.transition_model.move_left()
        self.most_recent_action = None

    def move_right(self):
        """Moves the agent to the right location."""
        self.transition_model.move_right()
        self.most_recent_action = None

    def action(self) -> Callable:
        """
        Updates the environment (state) based on the pervious action and
        decides the next action based on the current state.

        Returns:
            callable: The next action to be performed.
        """
        self.update_state()
        if self.sensor_model.sense_dirt():
            self.most_recent_action = self.suck
        elif self.sensor_model.sense_location_id() == "A":
            self.most_recent_action = self.move_right
        elif self.sensor_model.sense_location_id() == "B":
            self.most_recent_action = self.move_left
        return self.most_recent_action

    def update_state(self):
        """Updates the state of the environment based on the most recent action."""
        if self.most_recent_action is not None:
            self.most_recent_action()
        self.most_recent_action = None


def main():
    """Runs a simple simulation of the vacuum agent in a two-location environment."""
    # Define locations
    location_a = Location("A", dirt=True)
    location_b = Location("B", dirt=True)
    locations = {"A": location_a, "B": location_b}

    # Define movements
    movements = {
        "A": MovementModel(left="B", right="B"),
        "B": MovementModel(left="A", right="A"),
    }

    # Initialize state and models
    state = State(locations=locations, current_location_id="A")
    transition_model = TransitionModel(state=state, movements=movements)
    sensor_model = SensorModel(state=state)
    vacuum_agent = ModelReflexVacuum(state, transition_model, sensor_model)

    # Simulate agent actions
    for _ in range(5):
        action = vacuum_agent.action()
        if action:
            action()
        print(
            f"Current location: {state.current_location_id}, "
            f"Dirt: {state.current_location().dirt}"
        )


if __name__ == "__main__":
    main()
