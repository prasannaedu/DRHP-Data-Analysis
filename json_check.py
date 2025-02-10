import json

# Load the JSON file
json_file = "SAMBHV STEEL TUBES LIMITED_parsed.json"

try:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Print the first item to check its structure
    print(json.dumps(data[0], indent=2))

except FileNotFoundError:
    print(f"❌ File not found: {json_file}")
except json.JSONDecodeError as e:
    print(f"❌ Error reading JSON file: {e}")
