class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        def bt(path, current_sum):
            p = sorted(path[:])
            if current_sum > target or p in result:
                return

            if current_sum == target:
                result.append(p)
                return



            for num in nums[:]:
                path.append(num)
                bt(path, current_sum+num)
                path.pop()
        bt([], 0)
        return result


        