import math

record = float(input())  # in seconds
distance = float(input()) # in meters
time_for_one_meter = float(input()) # in seconds
needed_swim = distance * time_for_one_meter
slow = math.floor(distance / 15) * 12.5 # slow every 15 minutes ith 12.5 seconds

total = needed_swim + slow
if total < record:
    print(f" Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total-record):.2f} seconds slower.")