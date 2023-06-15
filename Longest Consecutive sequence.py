nums = [100,4,200,1,3,2,2]
numSet = set(nums)
print(numSet)
longest = 0

for n in numSet:
    # check if its the start of a sequence
    if (n - 1) not in numSet:
        length = 1
        while (n + length) in numSet:
            length += 1
        longest = max(length, longest)

print(longest)