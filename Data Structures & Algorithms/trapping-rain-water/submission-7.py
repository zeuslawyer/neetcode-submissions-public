class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]

        vol = 0 
        while left < right:
            # check the maxes only as that is what determines max trappable water level
            if leftMax < rightMax:
                left += 1
                leftMax= max(leftMax, height[left])

                # this if check is unecessary because we do max() before.  If this current 
                # height is the max, then leftMax - height[left] = 0
                if height[left] < leftMax:
                    vol += leftMax - height[left]
            
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                if rightMax > height[right]:
                    vol += rightMax - height[right]
            
        return vol

        