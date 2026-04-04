class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        m = {}
        s = 0
        for num in nums:
            s += num

        if s % 2 != 0:
            return False

        def dp(inp):

            if str(inp) in m:
                 total_sum = m[str(inp)]
            else:
                total_sum = 0
                for num in inp:
                    total_sum += num
                m[str(inp)] = total_sum

            if total_sum == s//2:
                return True
                 
            for i in range(len(inp)):
                tmp_inp = inp.copy()
                del tmp_inp[i]
                print(tmp_inp)
                if dp(tmp_inp):
                    return True
            return False
        a = dp(nums)
        # print(m)
        # print(a)
        return a



        