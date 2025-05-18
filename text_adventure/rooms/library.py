from .basement import Room

class Library(Room):
    """A dusty library with towering bookshelves. Exits lead to the kitchen (south) and basement (east).
    
    Attributes:
        description: Text description of the room
        exits: Dictionary of available exits (direction: destination)
    """
    
    def __init__(self):
        super().__init__(
            description="A dusty library with towering bookshelves.",
            exits={"south": "kitchen", "east": "basement"}
        )