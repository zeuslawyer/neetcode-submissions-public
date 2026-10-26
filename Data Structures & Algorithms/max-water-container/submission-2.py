class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxvol = 0

        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            maxvol = max(maxvol, area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        

        return maxvol

