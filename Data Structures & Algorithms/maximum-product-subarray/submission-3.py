class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            tmp = cur_max
            cur_max = max(nums[i]*tmp, nums[i]*cur_min, nums[i])
            cur_min = min(nums[i]*tmp, nums[i]*cur_min, nums[i])

            if cur_max>global_max:
                global_max = cur_max
        return global_max

            

        