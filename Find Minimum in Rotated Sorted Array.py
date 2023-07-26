class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = ((r+l) // 2)
            if  nums[m] > nums[l] and nums[m] > nums[r]:
                l = m
            elif nums[m] < nums[r]:
                r = m
            else:
                return min(nums[l], nums[r])