# Chess Player Movement Simulation

A simple Python project demonstrating abstraction, inheritance, and polymorphism using the `abc` module.

## Features

- Defines an abstract `Player` base class.
- Tracks a player's position and movement history.
- Randomly selects valid moves.
- Implements a `Pawn` class with its own movement rules.
- Supports leveling up, allowing the pawn to move diagonally in addition to its original directions.

## Technologies

- Python 3
- abc (Abstract Base Classes)
- random

## Project Structure

```
.
└── main.py
```

## How It Works

- Every player starts at position `(0, 0)`.
- Each move is randomly selected from the player's available moves.
- Every visited position is stored in the player's path.
- Calling `level_up()` expands the pawn's movement options to include diagonal movement.

## Example

```python
pawn = Pawn()

print(pawn.position)
# (0, 0)

pawn.make_move()
print(pawn.position)

pawn.level_up()

pawn.make_move()
print(pawn.path)
```

## Concepts Demonstrated

- Abstract Classes
- Inheritance
- Method Overriding
- Random Movement
- State Management