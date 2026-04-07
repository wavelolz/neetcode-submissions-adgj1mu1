import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.neg_num = [-1*n for n in nums]
        self.k = k
        heapq.heapify(self.neg_num)

    def add(self, val: int) -> int:
        heapq.heappush(self.neg_num, -val)
        neg_num_c = self.neg_num.copy()
        for i in range(self.k):
            r = heapq.heappop(neg_num_c)
        return -r
        # print(neg_num_c)
        # print(self.neg_num)
