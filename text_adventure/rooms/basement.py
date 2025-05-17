class Room:
    """Base class for all rooms in the game."""
    def __init__(self, description: str, exits: dict):
        self.description = description
        self.exits = exits

class Basement(Room):
    """A dark basement with a single flickering light.
    
    Attributes:
        description: Text description of the room
        exits: Dictionary of available exits (direction: destination)
    """
    def __init__(self):
        super().__init__(
            description="A dark basement with a single flickering light.",
            exits={"west": "Library"}
        )