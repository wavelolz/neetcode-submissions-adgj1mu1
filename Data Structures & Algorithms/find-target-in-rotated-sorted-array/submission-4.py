class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<high:
            mid = low + (high-low)//2

            if nums[mid]>nums[high]:
                low = mid+1
            else:
                high = mid
        first = nums[:low]
        second = nums[low:]

        if target<=second[-1]:
            low = 0
            high = len(second)-1
            target_s = second
            b = len(first)
        else:
            low = 0
            high = len(first)-1
            target_s = first
            b = 0

        while low<high:
            mid = low + (high-low)//2
            if target_s[mid]<target:
                low = mid+1
            elif target_s[mid]>target:
                high = mid
            else:
                return b+mid

        if nums[b+low] == target:
            return b+low
        else:
            return -1
        


        