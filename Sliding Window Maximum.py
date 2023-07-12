#my_sol:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        lis = []
        queue = []
        queue.append(nums[0])
        for i in range(1,k,1):
            while nums[i] > queue[-1]:
                queue.pop()
                if not queue:
                    break
            queue.append(nums[i])
        lis.append(queue[0])
        L = 1
        R = k
        while R < len(nums):
            if nums[L-1] == queue[0]:
                queue.pop(0)
            while nums[R] > queue[-1]:
                queue.pop()
                if not queue:
                    break
            queue.append(nums[R])
            lis.append(queue[0])
            L = L+1
            R = R+1
        return lis

#opt sol:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
