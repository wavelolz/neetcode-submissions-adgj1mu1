class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        c1 = [-1]*n; c2 = [-1]*n; c3 = [-1]*n

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
            
        c1[0] = nums[0]        
        c1[1] = nums[0]
        for i in range(2, n-1):
            c1[i] = max(c1[i-2]+nums[i], c1[i-1])
        c1[n-1] = c1[n-2]

        c2[0] = 0        
        c2[1] = nums[1]
        for i in range(2, n-2):
            c2[i] = max(c2[i-2]+nums[i], c2[i-1])
        c2[n-2] = c2[n-3]
        c2[n-1] = c2[n-2]+nums[n-1]

        c3[0] = 0        
        c3[1] = nums[1]
        for i in range(2, n-1):
            c3[i] = max(c3[i-2]+nums[i], c3[i-1])
        c3[n-1] = c3[n-2]

        return max(c1[n-1], c2[n-1], c3[n-1])