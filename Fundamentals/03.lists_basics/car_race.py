string = input().split()
times = [int(x) for x in string]

# Calculate the middle index, which is the finish line
mid_index = len(times) // 2

# Initialize times for the two cars
left_car_time = 0
right_car_time = 0

first_half = times[:mid_index]
# Calculate the total time for the left car (from the start to the finish line)
for time in first_half:
    if time == 0:
        left_car_time -= left_car_time * 0.20  # Reduce time by 20% if time is 0
    else:
        left_car_time += time

#To get elements from the last element to the middle (not inclusive) ([::-1] to get them reversed from back to mid)
second_half = times[mid_index + 1:][::-1]
for time in second_half:
    if time == 0:
        right_car_time -= right_car_time * 0.20  # Reduce time by 20% if time is 0
    else:
        right_car_time += time

# Determine the winner and print the result
if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")