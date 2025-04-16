# Initialize dictionary for key materials and set their starting values to 0
key_materials = {"shards": 0, "fragments": 0, "motes": 0}

# Initialize an empty dictionary for junk materials
junk = {}

# Mapping of key materials to legendary items
legendary_map = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

# This will store the name of the legendary item once it's obtained
legendary_item = ""
obtained = False  # Flag to stop the loop once a legendary is crafted

# Start reading input lines until a legendary item is obtained
while not obtained:
    # Read a line of input and make all materials lowercase for consistency
    parts = input().lower().split()

    # Process the input in pairs: quantity and material
    for i in range(0, len(parts), 2):
        qty = int(parts[i])            # Convert quantity to integer
        material = parts[i + 1]        # Get the material name

        # If it's a key material, update its quantity
        if material in key_materials:
            key_materials[material] += qty

            # Check if this material reached the threshold for a legendary item
            if key_materials[material] >= 250:
                legendary_item = legendary_map[material]  # Get the item name
                key_materials[material] -= 250            # Use up 250 units
                obtained = True                           # Set flag to stop loop
                print(f"{legendary_item} obtained!")      # Print the result
                break  # Exit inner loop immediately

        else:
            # If it's junk material, store or update its count
            if material not in junk:
                junk[material] = 0
            junk[material] += qty

# Print key materials in fixed order
for mat in ["shards", "fragments", "motes"]:
    print(f"{mat}: {key_materials[mat]}")

# Print junk in the order it was added
for mat in junk:
    print(f"{mat}: {junk[mat]}")