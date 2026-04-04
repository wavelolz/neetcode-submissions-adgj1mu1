class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 1e5
        s = 0
        mp = 0

        for i in range(len(prices)):
            if prices[i]<b:
                b = prices[i]
                s = prices[i]
                continue
            
            if prices[i]>s:
                s = prices[i]
            
            if s-b > mp:
                mp = s-b
        return mp

        