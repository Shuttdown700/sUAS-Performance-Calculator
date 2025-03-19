import json
import os

def load_json_data(directory="components"):
    """Loads all JSON component files from the specified directory."""
    assert isinstance(directory,str) and len(directory) > 0, "Relative directory must be a string of at least length 1 "
    data = {}
    directory = os.path.join(os.path.dirname(__file__), directory)
    if not os.path.exists(directory):
        print(f"Warning: Directory '{directory}' not found.")
        return data
    
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            category = filename.split("_options")[0]
            with open(os.path.join(directory, filename), "r") as file:
                try:
                    data[category] = json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Error loading {filename}: {e}")
    if len(os.listdir(directory)) == 0:
        print(f"Warning: No .json files in directory: '{directory}'.")
    return data

if __name__ == "__main__":
    components = load_json_data("components")
    for category, items in components.items():
        print(f"Loaded {len(items)} {category} options.")
