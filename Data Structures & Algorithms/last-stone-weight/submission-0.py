import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            h1 = heapq.heappop(stones)
            h2 = heapq.heappop(stones)
            heapq.heappush(stones, h1-h2)
        return -1*stones[0]
        