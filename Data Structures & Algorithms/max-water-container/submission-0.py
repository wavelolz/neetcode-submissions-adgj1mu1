class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights)-1
        max_area = 0

        while s < e:
            area = (e-s)*min(heights[s], heights[e])
            if area > max_area:
                max_area = area
            
            if heights[s] < heights[e]:
                s += 1
            else:
                e -= 1
        return max_area
        