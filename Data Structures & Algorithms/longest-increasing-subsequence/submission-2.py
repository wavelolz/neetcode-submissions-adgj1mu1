class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [-1]*len(nums)
        arr[0] = 1

        for i in range(1, len(nums)):
            longest = 1
            for j in range(i):
                if nums[i]>nums[j] and arr[j]+1>longest:
                    longest = arr[j]+1
            arr[i] = longest
        print(arr)
        return max(arr)
        