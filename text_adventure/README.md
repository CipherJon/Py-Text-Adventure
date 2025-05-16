# Python Text Adventure Game

A classic text-based adventure game implementation.

## Features
- Multiple interconnected rooms
- JSON-based story configuration
- Simple navigation system

## Installation
```bash
Clone the repository
git clone https://github.com/username/text-adventure.git cd text-adventure

Install dependencies (if any)
pip install -r requirements.txt
```

## Running the Game
```bash
python text_adventure/adventure.py
```

## Game Commands
- `go [direction]`: Move in a direction (north, south, east, west)
- `look`: Examine the current room
- `quit`: Exit the game

## Creating Custom Stories
The game uses a JSON file (`data/story.json`) to define rooms and connections:
```json
{
  "rooms": {
    "kitchen": {
      "description": "A messy kitchen with strange smells",
      "exits": {"north": "library"}
    },
    ...
  }
}