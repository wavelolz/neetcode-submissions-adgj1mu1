class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []

        def bt(path, current_sum, inx):
            print(path, current_sum, inx)
            if current_sum == target:
                s_path = sorted(path)
                if not s_path in result:
                    result.append(path[:])
                return

            for j in range(inx, len(candidates)):
                if current_sum + candidates[j] > target:
                    return

                path.append(candidates[j])
                bt(path, current_sum+candidates[j], j+1)
                path.pop()
        bt([], 0, 0)
        return result


        