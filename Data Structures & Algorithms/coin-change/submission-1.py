class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = {}
        def dp(inx):
            if inx in m.keys():
                return m[inx]

            if inx < 0:
                m[inx] = -1
                return -1
            elif inx == 0:
                m[inx] = 0
                return 0

            candidates = [0]*len(coins)
            
            for i in range(len(coins)):
                candidates[i] = dp(inx-coins[i])

            if all(num < 0 for num in candidates):
                m[inx] = -1
                return -1
            else:
                m[inx] = min([num for num in candidates if num >= 0])+1 
                return min([num for num in candidates if num >= 0])+1 
        return dp(amount)
        
            

            
