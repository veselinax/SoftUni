numbers = list(map(lambda x: int(x),input().split(", ")))
pos = [str(num) for num in numbers if num >= 0]
neg = [str(num) for num in numbers if num < 0]
even = [str(num) for num in numbers if num % 2 == 0]
odd = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(pos)}")
print(f"Negative: {', '.join(neg)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")