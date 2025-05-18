import os
from text_adventure.utils import load_story_data
from text_adventure.rooms.kitchen import Kitchen
from text_adventure.rooms.library import Library
from text_adventure.rooms.basement import Basement

def main():
    # Dynamic path
    story_path = os.path.join(os.path.dirname(__file__), 'data', 'story.json')
    print("Looking for file at:", story_path)  # Debug
    story_data = load_story_data(story_path)
    ROOM_CLASSES = {
        "kitchen": Kitchen,
        "library": Library,
        "basement": Basement
    }
    current_room = ROOM_CLASSES["kitchen"]()
    
    print("Welcome to the Text Adventure Game!")
    
    while True:
        print(f"\n{current_room.description}")
        print("Exits:", ", ".join(current_room.exits.keys()))
        
        command = input("Where would you like to go? ").lower()
        if command in current_room.exits:
            next_room = current_room.exits[command]
            if next_room in story_data["rooms"]:
                current_room = ROOM_CLASSES[next_room]()
            else:
                print("You can't go that way!")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()