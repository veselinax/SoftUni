d = int(input())
s = int(input())
v = int(input())
percentage_taken = float(input())
volume = d * s * v  # cm³
liters_to_fit = volume * 0.001  # 1 cm³ = 0.001 L   same as /1000
percent = percentage_taken * 0.01  # same as /100
liters_needed = liters_to_fit * (1 - percent)
print(f"{liters_needed:.3f}")