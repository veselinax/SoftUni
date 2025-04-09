import math

year_type = input()
holidays_count = int(input())  # not weekends
weekends_home = int(input())

weekends = 48
weekends_in_sofia = weekends - weekends_home
saturday_games = weekends_in_sofia * 3/4  #не е на работа 3/4 от уикендите и играе
sunday_games = weekends_home
holiday_games = holidays_count * 2/3   # играе 2/3 от празничните дни
total_games = saturday_games + sunday_games + holiday_games

if year_type == "leap":
    total_games += total_games * 0.15
print(f"{math.floor(total_games)}")