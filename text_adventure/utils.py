import json

class Room:
    def __init__(self, room_data):
        self.description = room_data['description']
        self.exits = room_data['exits']

def load_story_data(file_path: str) -> dict:
    """Load story data from a JSON file.
    
    Args:
        file_path: Path to the JSON file to load
        
    Returns:
        A dictionary containing the loaded JSON data
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {file_path}") from e