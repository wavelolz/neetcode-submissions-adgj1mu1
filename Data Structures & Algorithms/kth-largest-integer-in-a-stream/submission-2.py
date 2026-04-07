import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num = nums
        heapq.heapify(self.num)
        self.k = k
        while len(self.num) > k:
            heapq.heappop(self.num)

    def add(self, val: int) -> int:
        heapq.heappush(self.num, val)
        while len(self.num) > self.k:
            heapq.heappop(self.num)
        return self.num[0]

