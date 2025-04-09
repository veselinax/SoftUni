student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while True:
    movie_name = input()  # Името на филма
    if movie_name == "Finish":
        break  # Ако командата е "Finish", прекратяваме програмата

    free_seats = int(input())  # Свободни места в залата за този филм
    current_movie_tickets = 0  # Броя на закупените билети за текущия филм

    while True:
        ticket_type = input()  # Тип на закупен билет
        if ticket_type == "End":
            break  # Ако командата е "End", приключваме продажбите за този филм

        current_movie_tickets += 1
        total_tickets += 1

        # Броим продажбата на съответния тип билет
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if current_movie_tickets == free_seats:
            break  # Ако всички места са запълнени, приключваме с продажбите за този филм

    # Изчисляваме процента на запълненост на залата
    occupancy_percentage = (current_movie_tickets / free_seats) * 100
    print(f"{movie_name} - {occupancy_percentage:.2f}% full.")

# След като получим командата "Finish", изчисляваме и отпечатваме статистиката
student_percentage = (student_tickets / total_tickets) * 100
standard_percentage = (standard_tickets / total_tickets) * 100
kid_percentage = (kid_tickets / total_tickets) * 100 

print(f"Total tickets: {total_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kid_percentage:.2f}% kids tickets.")
