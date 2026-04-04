class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0
        for v in piles:
            if v>max_val:
                max_val = v
        
        left = 1
        right = max_val+1
        min_k = float("inf")
        while left<=right:
            k = left + (right-left) // 2
            total_hours = 0
            for j in piles:
                total_hours += (j + k - 1) // k

            if total_hours > h:
                left = k+1
            elif total_hours <= h:
                if k < min_k:
                    min_k = k
                right = k-1
        return min_k
        