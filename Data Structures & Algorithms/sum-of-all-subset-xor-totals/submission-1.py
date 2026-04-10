from typing import List
import heapq  # (not used, but kept since you included it)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        results = []
        total = 0
        def bt(path, idx, total):
            if idx == len(nums):
                results.append(total)
                return 

            # include nums[idx]
            path.append(nums[idx])
            bt(path, idx + 1, total ^ nums[idx])
            path.pop()

            # exclude nums[idx]
            bt(path, idx + 1, total)

        bt([], 0, total)

        ans = 0
        for val in results:
            ans += val

        return ans