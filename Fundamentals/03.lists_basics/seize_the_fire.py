fires = input().split("#")
water = int(input())
string = " = ".join(fires) # High = 89 = Low = 28 = Medium = 77 = Low = 23
my_list = string.split(" = ")  # ['High', '89', 'Low', '28', 'Medium', '77', 'Low', '23']
effort = 0
total_fire = 0
fire_details = []



for i in range(0, len(my_list), 2):
    type_of_fire = my_list[i]  # This gets the fire type
    value_of_cell = int(my_list[i + 1])  # This gets the corresponding value (convert it to integer)

    # Check if the fire cell is valid based on its type and value
    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        if water >= value_of_cell: # Check if there is enough water to put out the fire
            water -= value_of_cell # Reduce the water by the fire's value
            total_fire += value_of_cell # Add the fire's value to the total fire put out
            effort += 0.25 * value_of_cell # Add effort to the total (25% of the fire value)
            fire_details.append(value_of_cell)  # Add only the value of the fire to the list

    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        if water >= value_of_cell:
            water -= value_of_cell
            total_fire += value_of_cell
            effort += 0.25 * value_of_cell
            fire_details.append(value_of_cell)  # Add only the value of the fire to the list

    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        if water >= value_of_cell:
            water -= value_of_cell
            total_fire += value_of_cell
            effort += 0.25 * value_of_cell
            fire_details.append(value_of_cell)  # Add only the value of the fire to the list
print("Cells:")
for fire in fire_details:
    print(f" - {fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

#another way at the start and down same
#fires = input().split("#")  # Example input: "High = 89#Low = 28#Medium = 77#Low = 23"
#water = int(input())  # The amount of water available to put out fires.

# Initialize variables for tracking effort, total fire put out, and fire details (values of extinguished fires).
#effort = 0
#total_fire = 0
#fire_details = []  # This list will store the values of the successfully extinguished fires.

#for fire in fires:
    #type_of_fire, value_of_cell = fire.split(" = ")  # Split the fire type and value (e.g. 'High' and '89')
    #value_of_cell = int(value_of_cell)  # Convert the fire value to an integer.