class Solution:

    def trap(self, height: List[int]) -> int:
        def summer(x, y):
            if x - y < 0:
                return 0
            else:
                return x -y
        left = 0
        right = len(height) -1
        max_l = height[left]
        max_r = height[right]

        water = 0
        while left < right:
            if max_l < max_r:
                left = left + 1
                water = water + summer(max_l, height[left])
                max_l = max(max_l, height[left])   
            else:
                right = right - 1
                water = water + summer(max_r, height[right])
                max_r = max(max_r, height[right])
        return water

