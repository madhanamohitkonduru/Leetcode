class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        res = max(nums)

        for i in nums:
            if i == 0:
                curMax, curMin = 1,1
                continue
            temp = i* curMax
            curMax = max(temp, i* curMin, i)
            curMin = min(temp, i* curMin, i)
            res = max(res, curMax)
        return res