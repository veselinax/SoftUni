results = {}  # Keeps highest score for each student (excluding banned ones)
submissions = {}  # Tracks how many times each language was submitted

while True:
    command = input()
    if command == "exam finished":
        break

    parts = command.split("-")

    if parts[1] == "banned":
        user = parts[0]
        if user in results:
            results.pop(user)  # remove the student from the results
    else:
        user = parts[0]
        language = parts[1]
        points = int(parts[2])

        # Update submissions count
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1    # Keeps a count of how many times each language was submitted (even if it's from the same student)

        # Store the best score for each user
        if user not in results:
            results[user] = points
        else:
            results[user] = max(results[user], points)

# Print results
print("Results:")
for user, score in results.items():
    print(f"{user} | {score}")

# Print submissions
print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
