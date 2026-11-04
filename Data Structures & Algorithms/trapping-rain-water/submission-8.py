class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftMax, rightMax = height[0], height[len(height)-1]

        vol = height[left]-leftMax

        while left < right:
            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax, height[left])
                vol += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                vol += rightMax - height[right]
        return vol


