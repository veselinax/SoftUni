exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
# Преобразуваме времето в минути
exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

# Изчисляваме разликата в минути
time_difference = arrival_time_in_minutes - exam_time_in_minutes

# Определяме какво да изведем
if time_difference > 0:
    print("Late")
    hours_late = time_difference // 60
    minutes_late = time_difference % 60
    if hours_late >= 1:
        print(f"{hours_late}:{minutes_late:02d} hours after the start")
    else:
        print(f"{minutes_late} minutes after the start")
elif time_difference >= -30:
    print("On time")
    # Ако пристигне точно в същия час на изпита, не показваме минутите
    if arrival_hour != exam_hour or arrival_minute != exam_minute:
        print(f"{abs(time_difference)} minutes before the start")
else:
    print("Early")
    time_difference = abs(time_difference)
    hours_early = time_difference // 60
    minutes_early = time_difference % 60
    if hours_early >= 1:
        print(f"{hours_early}:{minutes_early:02d} hours before the start")
    else:
        print(f"{minutes_early} minutes before the start")

#The :02d format specifier is used in Python to format numbers with leading zeros if the number is less than 10
# d: This stands for "decimal integer," meaning it's for formatting integers
# :02: This specifies that the number should be padded with leading zeros to ensure it has at least two digits