class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(n):
            z = nums[i]
            m = {}
            for j in range(n):
                # print(m)
                # print()
                if j == i:
                    continue
                if -z-nums[j] in m:
                    # found answer
                    a = sorted([z, nums[j], -z-nums[j]])
                    if a not in ans:
                        ans.append(a)
                else:
                    m[nums[j]] = j
        return ans

        