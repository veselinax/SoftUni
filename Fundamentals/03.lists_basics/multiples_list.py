factor = int(input())
count = int(input())
nums = []

for num in range(factor, factor * count + 1, factor):  #We add +1 to ensure that factor * count is included in the range with step factor
    nums.append(num)
print(nums)