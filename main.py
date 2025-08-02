import re
import json
from pathlib import Path

def parse_level_input_txt(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    # Extract values using regex
    level = int(re.search(r"Level Number:\s*(\d+)", text).group(1))
    size = re.search(r"Zoo Size:\s*(\d+x\d+)", text).group(1)
    resources = eval(re.search(r"Available Resources:\s*(\[.*?\])", text).group(1))
    grid_str = re.search(r"Base Zoo:\s*(\[[\s\S]*\])", text).group(1)

    # Turn grid string into Python list
    grid = eval(grid_str)

    return {
        "level": level,
        "zoo_size": size,
        "resources": resources,
        "zoo": grid
    }

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved to {path}")

def main():
    input_path = Path("data/level_1_input.txt")
    output_path = Path("data/level_1_output.json")

    zoo_data = parse_level_input_txt(input_path)
    
    print(f"📋 Level: {zoo_data['level']}")
    print(f"📐 Grid size: {zoo_data['zoo_size']}")
    print(f"🦁 Available Resource IDs: {zoo_data['resources']}")
    
    save_json(zoo_data, output_path)

if __name__ == "__main__":
    main()
