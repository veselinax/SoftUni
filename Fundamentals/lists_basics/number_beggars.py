nums_str = input().split(", ")  # separating by comma and a space and making a list
beggars = int(input())
nums = []

for num in nums_str:
    nums.append(int(num)) # converting the str num to int and adding to the list
result_sum = [0] * beggars # This list will store the sum of numbers for each beggar.\
# Initially, every beggar has a sum of 0
for i in range(len(nums)):
    index = i % beggars  #The expression i % count ensures that the beggars get the numbers in a round-robin fashion (after the first participant receives their turn, the next participant gets their turn, and so on. Once the last participant has received their turn, the process starts again from the first participant. This pattern repeats as necessary, ensuring fairness and balance)
    result_sum[index] += nums[i] #The number from nums[i] is added to the sum of the appropriate beggar (determined by index)
    # So, the number nums[i] is assigned to the corresponding beggar’s total sum
print(result_sum)