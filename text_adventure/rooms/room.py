# text_adventure/rooms/room.py
class Room:
    def __init__(self, description="", exits=None):
        self.description = description
        self.exits = exits if exits is not None else {}

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits