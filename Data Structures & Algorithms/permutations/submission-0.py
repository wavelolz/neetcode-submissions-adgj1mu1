class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def bt(path, current_inx):
  
            if len(path) == len(nums):
                result.append(path[:])
                return


            for j in range(len(nums)):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                bt(path, 0)
                path.pop()
        bt([], 0)
        return result

        