start_points = int(input())
bonus = 0
if start_points <= 100:
    bonus += 5
elif  100 < start_points < 1000:
    bonus += (start_points * 0.20)  # to the bonus we add 20 % of the starting points
else:
    bonus += (start_points * 0.10)  # to the bonus we add 10 % of the starting points

if start_points % 2 == 0:
    bonus += 1
elif str(start_points)[-1] == "5":    #converts the number to string and checks if last digit (index [-1]) is 5 or num % 10 == 5 is same
    bonus += 2

print(bonus)
print(bonus + start_points)