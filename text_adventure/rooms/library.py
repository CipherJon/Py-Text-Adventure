class Library:
    """A dusty library with towering bookshelves. Exits lead to the kitchen (south) and basement (east)."""
    
    def __init__(self):
        self.description = "A dusty library with towering bookshelves."
        self.exits = {"south": "kitchen", "east": "basement"}