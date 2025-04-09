time_1 = int(input())  # in seconds
time_2 = int(input())
time_3 = int(input())
total_time = time_1 + time_2 +time_3  #total seconds
minutes = total_time // 60  #celochisleno delene za da vzemem minutite
seconds = total_time % 60  #ostatuk za da vzemem sekundite
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
