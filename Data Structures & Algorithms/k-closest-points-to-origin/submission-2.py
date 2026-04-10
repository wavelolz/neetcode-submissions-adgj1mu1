from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        
        for i in range(len(points)):
            x, y = points[i]
            dist = -(x**2 + y**2)
            heapq.heappush(arr, (dist, points[i]))
            while len(arr) > k:
                heapq.heappop(arr)
        ans = []
        for i in range(k):
            ans.append(arr[i][1])

        return ans