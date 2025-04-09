judges_count = int(input())  # Number of judges
presentation_name = input()  # First presentation
total_sum = 0  # Accumulating the total sum of grades
total_grades_count = 0  # Total number of grades across all presentations

while presentation_name != "Finish":
    current_sum = 0  # Sum of the grades for the current presentation

    for i in range(judges_count):
        grade = float(input())  # Read grade from a judge
        current_sum += grade  # Add grade to the total sum for the presentation

    # Calculate the average for the current presentation
    average_grade = current_sum / judges_count

    # Add the average grade of the current presentation to the total sum
    total_sum += current_sum  # We add all grades, not the average here
    total_grades_count += judges_count  # Count all grades (for all presentations)

    # Print the average grade for the current presentation
    print(f"{presentation_name} - {average_grade:.2f}.")

    # Read the name of the next presentation
    presentation_name = input()

# When "Finish" is entered, print the final assessment
if presentation_name == "Finish":
    # Calculate the overall average by dividing total_sum by total_grades_count
    final_average = total_sum / total_grades_count
    print(f"Student's final assessment is {final_average:.2f}.")
