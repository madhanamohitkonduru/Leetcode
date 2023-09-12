class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            first, second = heapq.heappop(stones) * -1, heapq.heappop(stones) * -1
            if second < first:
                heapq.heappush(stones, (first - second) * -1)

        if stones:
            return stones[0] * -1
        else:
            return 0