# SimpleReflexVacuum: A robot vacuum cleaner modeled as a simple reflex agent.
# Your implementation should pass the tests in test_simple_reflex_vacuum.py.
# Aliyeh Ebrahimi
from typing import Dict, Union, Callable, Tuple


class SimpleReflexVacuum:
    """
    A simple reflex agent for a vacuum cleaner.

    Attributes:
        rules (Dict[Tuple[str, Union[str, None]], Callable]):
            A dictionary defining the rules for the agent's behavior based on location and dirt status.
    """

    def __init__(
        self, rules: Union[Dict[Tuple[str, Union[str, None]], Callable], None] = None
    ):
        """
        Initializes the SimpleReflexVacuum with predefined or custom rules.

        Args:
            rules (Dict[Tuple[str, Union[str, None]], Callable], optional):
                Custom rules mapping (location, dirt status) to actions. Defaults to None.
        """
        self.rules = rules or {
            ("A", "Dirt"): self.suck,
            ("A", None): self.move_right,
            ("B", "Dirt"): self.suck,
            ("B", None): self.move_left,
        }

    def suck(self):
        """Cleans the dirt at the current location."""
        return None

    def move_right(self):
        """Moves the agent to the right location."""
        return "B"

    def move_left(self):
        """Moves the agent to the left location."""
        return "A"

    def action(self, location_id: str, dirt: Union[str, None]) -> Callable:
        """
        Determines the next action based on the current location and dirt status.

        Args:
            location_id (str): The ID of the current location.
            dirt (Union[str, None]): The dirt status at the current location ("Dirt" or None).

        Returns:
            Callable: The action to be performed (suck, move_right, or move_left).
        """
        return self.rules[(location_id, dirt)]


def main():
    """Runs a simple simulation of the SimpleReflexVacuum agent."""
    # Initialize the agent
    agent = SimpleReflexVacuum()

    # Define a simple environment
    environment = [
        {"location_id": "A", "dirt": "Dirt"},
        {"location_id": "A", "dirt": None},
        {"location_id": "B", "dirt": "Dirt"},
        {"location_id": "B", "dirt": None},
    ]

    # Simulate agent actions
    for step, state in enumerate(environment):
        location_id = state["location_id"]
        dirt = state["dirt"]
        action = agent.action(location_id, dirt)
        result = action()
        print(
            f"Step {step + 1}: Location {location_id}, Dirt: {dirt}, Action Result: {result}"
        )


if __name__ == "__main__":
    main()
