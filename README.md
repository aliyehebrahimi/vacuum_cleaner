# Vacuum-Cleaner World Simulation

This project explores the design and implementation of reflex agents within a two-location Vacuum-Cleaner World. It demonstrates the differences between simple reflex agents and model-based reflex agents, highlighting their decision-making processes and how they interact with their environment.

## Overview

The Vacuum-Cleaner World consists of two locations, each of which may be clean or dirty. An intelligent agent, in the form of a vacuum cleaner, must navigate between these locations and decide on appropriate actions based on its percepts.

Two agent implementations are developed:
- **Simple Reflex Agent**: Reacts purely based on the current percept, without maintaining an internal state.
- **Model-Based Reflex Agent**: Maintains an internal model of the world and updates its state over time to make informed decisions.

## Implementation Details

### Simple Reflex Agent

The **SimpleReflexVacuum** agent is implemented in `simple_reflex_vacuum.py`. This agent makes decisions based only on its immediate percept, without considering past information.

Key characteristics:
- Uses an `if`-`elif` conditional structure to determine actions.
- Receives percepts that indicate whether a location is dirty and the agent's current position.
- Performs a `suck` action when dirt is detected.
- Moves left or right if the current location is clean.

To verify the implementation, run:
```sh
python3 test_simple_reflex_vacuum.py
```

### Model-Based Reflex Agent

The **ModelReflexVacuum** agent is implemented in `model_reflex_vacuum.py`. Unlike the simple reflex agent, this implementation incorporates a model of the environment, allowing it to track the state of both locations.

Key characteristics:
- Maintains an internal representation of the world state.
- Utilizes a transition model and sensor model to update its state.
- Makes decisions based on both current and past percepts.
- Adheres to the model-based reflex agent design specified in the AIMA book (Figure 2.12).

## Running the Simulation

To observe both agents in action, execute:
```sh
python3 main.py
```
This script demonstrates how the agents interact with their environment and make decisions based on their respective designs.



