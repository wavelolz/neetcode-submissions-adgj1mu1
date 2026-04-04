class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        mp = 0

        for p in prices:
            mp = max(mp, p-b)
            b = min(b, p)
        return mp

        