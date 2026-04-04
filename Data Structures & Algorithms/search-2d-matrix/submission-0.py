class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                nums.append(matrix[i][j])

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = r + (l-r)//2

            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                return True
        return False

        