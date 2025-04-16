hour = int(input())
minutes = int(input())
minutes += 15  
if minutes  >= 60:
    hour += 1      # we have one more hour
    minutes -= 60  # we remove it from the minutes
    if hour == 24:
        hour = 00
if minutes <= 9:
    print(f"{hour}:0{minutes}")   # so we start with 0 (01, 02, 03 etc)
else:
    print(f"{hour}:{minutes}")