class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       arr = [1e5]*(amount+1)
       arr[0] = 0
       for i in range(1, amount+1):
        for coin in coins:
            if i-coin>=0:
                arr[i] = min(arr[i], arr[i-coin]+1)
       print(arr)
       return arr[amount] if arr[amount]<1e5 else -1
            

            
