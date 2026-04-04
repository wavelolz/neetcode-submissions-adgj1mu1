class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lidx = 0
        ridx = len(numbers)-1

        while lidx < ridx:
            s = numbers[lidx]+numbers[ridx] 
            if s == target:
                return [lidx+1, ridx+1]
            elif s < target:
                lidx += 1
            else:
                ridx -= 1
            