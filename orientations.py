import json

# Load JSON file
with open('resource.json', 'r') as file:
    resource_data = json.load(file)

# Extract bounding box
bounding_box = resource_data["bounding_box"]

# Extract orientations
def get_orientation_grids(resource):
    grids = {}
    for orientation in resource["orientations"]:
        rotation = orientation["rotation"]
        cells = orientation["cells"]

        # Initialize a blank grid
        grid = [[0 for _ in range(bounding_box)] for _ in range(bounding_box)]

        # Fill grid based on cells
        for row, col in cells:
            grid[row][col] = 1

        grids[rotation] = grid
    return grids

# Get grids for each orientation
orientation_grids = get_orientation_grids(resource_data)

# Print each orientation grid
for rotation, grid in orientation_grids.items():
    print(f"\nRotation {rotation}:")
    for row in grid:
        print(" ".join(str(cell) for cell in row))