from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [0] * len(points)
        
        for i in range(len(points)):
            x, y = points[i]
            dist = x**2 + y**2
            arr[i] = (dist, points[i])
        
        heapq.heapify(arr)
        
        ans = [0] * k
        for i in range(k):
            dist, p = heapq.heappop(arr)
            ans[i] = p
        
        return ans