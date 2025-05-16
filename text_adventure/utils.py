def load_story_data(file_path):
    """Load story data from a JSON file."""
    import json
    with open(file_path, 'r') as f:
        return json.load(f)