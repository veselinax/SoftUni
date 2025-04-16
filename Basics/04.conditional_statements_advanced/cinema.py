projection_type = input()
rows_count = int(input())
columns_count = int(input())
price = 0

if projection_type == "Premiere":
    price = 12.00
elif projection_type == "Normal":
    price = 7.50
else:
    price = 5.00
total_price = price * rows_count * columns_count
print(f"{total_price:.2f} leva")