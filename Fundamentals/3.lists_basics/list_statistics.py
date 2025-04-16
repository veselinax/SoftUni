n = int(input())
pos = []
neg = []
pos_count = 0
neg_sum = 0

for i in range(n):
    integer = int(input())
    if integer >= 0:
        pos.append(integer)
        pos_count += 1
    else:
        neg.append(integer)
        neg_sum += integer
print(pos)
print(neg)
print(f"Count of positives: {pos_count}\nSum of negatives: {neg_sum}")  # new line for neg sum
# or we can just use len(pos) and sum(neg) 