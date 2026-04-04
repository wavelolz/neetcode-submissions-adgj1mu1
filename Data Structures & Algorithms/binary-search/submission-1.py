class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr = nums
        inx = []
        for i, val in enumerate(nums):
            inx.append(i)

        while len(arr)>0:
            midl = len(arr) // 2

            if target > arr[midl]:
                arr = arr[midl+1:]
                inx = inx[midl+1:]
            elif target < arr[midl]:
                arr = arr[:midl]
                inx = inx[:midl]
            else:
                return inx[midl]
        return -1
        