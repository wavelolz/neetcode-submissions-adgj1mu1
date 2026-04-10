from typing import List
import heapq  # (not used, but kept since you included it)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        results = []

        def bt(path, idx):
            if idx == len(nums):
                if len(path) == 0:
                    return
                elif len(path) == 1:
                    results.append(path[0])
                else:
                    s = 0
                    for n in path:
                        s ^= n
                    results.append(s)
                return

            # include nums[idx]
            path.append(nums[idx])
            bt(path, idx + 1)
            path.pop()

            # exclude nums[idx]
            bt(path, idx + 1)

        bt([], 0)

        ans = 0
        for val in results:
            ans += val

        return ans