dictionary = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break

    company = command[0]
    employee_id = command[1]

    if company not in dictionary:
        dictionary[company] = []

    # Only add the employee if not already added to that company
    if employee_id not in dictionary[company]:
        dictionary[company].append(employee_id)

# Print output
for company, employees in dictionary.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
