class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0]*len(cost)
        t = len(cost)-1
        for i in range(2, len(cost)):
            arr[i] = min(arr[i-1]+cost[i-1], arr[i-2]+cost[i-2])
        print(arr)
        return min(arr[t-1]+cost[t-1], arr[t]+cost[t])
        