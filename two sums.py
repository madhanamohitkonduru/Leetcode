#My solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c=0
        for i in range(len(nums)-1):
            if target-nums[i] in nums[i+1:]:
                n=nums[i+1:]
                return [i, n.index(target-nums[i])+len(nums)-len(n)]


#Proper solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
