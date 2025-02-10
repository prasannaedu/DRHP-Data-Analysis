import json
import os

def view_json(filename="parsed_data_with_structure.json", pretty=True):
    if not os.path.exists(filename):  # Check if the file exists
        print(f"Error: The file {filename} does not exist.")
        return
    
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            if pretty:
                print(json.dumps(data, indent=4))  # Pretty print with indentation
            else:
                print(json.dumps(data))  # Single-line format without indentation
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Optionally, pass a file path and whether to print in a pretty format
    view_json("parsed_data_with_structure.json", pretty=True)
