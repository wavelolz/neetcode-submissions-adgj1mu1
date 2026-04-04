class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(inx):

            if inx==len(nums):
                result.append(nums[:])
                return

            for i in range(inx, len(nums)):

                nums[i], nums[inx] = nums[inx], nums[i]

                bt(inx+1)

                nums[inx], nums[i] = nums[i], nums[inx]
        bt(0)
        return result