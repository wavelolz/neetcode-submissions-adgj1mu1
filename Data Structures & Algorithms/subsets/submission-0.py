class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        def bt(path, inx):
            if inx == len(nums):
                result.append(path[:])
                return
                
            path.append(nums[inx])
            bt(path, inx+1)
            path.pop()

            bt(path, inx+1)
        bt([], 0)
        return result