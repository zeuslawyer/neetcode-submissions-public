class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers. And capture the current max heights on either side.
        left, right = 0, len(height)-1
        leftMax, rightMax = height[0], height[len(height)-1]

        # starting vol should be 0, because height and max are equal.    
        vol = height[left]-leftMax

        while left < right:
        # the lower of the two max heights sets the max rain that can be trapped.
        #  we capture the current index height and update global max if needed. the differential is the volument at that index.
            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax, height[left])
                vol += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                vol += rightMax - height[right]
        return vol


