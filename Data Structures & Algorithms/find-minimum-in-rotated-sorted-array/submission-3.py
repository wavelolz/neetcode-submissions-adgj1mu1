class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high-low) // 2

            if nums[low]<=nums[mid] and nums[mid]<=nums[high]:
                return nums[low]
            elif nums[low]>=nums[mid] and nums[mid]>=nums[high]:
                return nums[high]
            if nums[mid]-nums[mid-1]<0:
                return nums[mid]
            else:
                if nums[low]<nums[mid]:
                    low = mid+1
                elif nums[mid]<nums[high]:
                    high = mid-1
            print(low, high)

            