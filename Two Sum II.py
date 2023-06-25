# #my soultion
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lis = []
        for i in range(len(numbers)):
            if numbers[i] in lis:
                return [lis.index(numbers[i])+1, i+1]
            lis.append(target-numbers[i])


numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9
# Time limit exceeded
for i in range(len(numbers)-1):
    for j in range(len(numbers)-1, 0, -1):
        if numbers[i] + numbers[j] == target:
            print([i+1, j+1])
        elif numbers[i] + numbers[j] > target:
            pass
        elif numbers[i] + numbers[j] < target:
            break


# Actual Solution
l = 0
r = len(numbers) - 1
while True:
    if numbers[l] + numbers[r] == target:
        print([l + 1, r + 1])
        break
    elif numbers[l] + numbers[r] > target:
        r -= 1
    elif numbers[l] + numbers[r] < target:
        l += 1
