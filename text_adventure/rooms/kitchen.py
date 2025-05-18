from text_adventure.rooms.room import Room

class Kitchen(Room):
    """A messy kitchen with strange smells. Exits lead to the library.

    Attributes:
        description: Text description of the room
        exits: Dictionary of available exits (direction: destination)
    """
    def __init__(self):
        super().__init__(
            description="A messy kitchen with strange smells.",
            exits={"north": "library"}
        )