nums_str = input().split()  # splitting the string by space and creating a list
nums = []

for num in nums_str:   # iterating the list
    nums.append(-int(num))  # adding - num
print(nums)