class Solution:
    def trap(self, height: List[int]) -> int:
        # We need:
        # height of current element AND
        # min of ( max heights recorded on left and right side)
        # min(l, r) - currHeight is num units of water that can be stored

        l, r = 0, len(height)-1
        maxHeightLeft, maxHeightRight = height[l], height[r]
        waterQty = 0

        while l < r:
            # increment pointer based of the side with lowest max height
            # as that represents the amount of water that can be trapped
            if maxHeightLeft < maxHeightRight:
                l += 1
                maxHeightLeft = max(maxHeightLeft, height[l])
                waterQty += maxHeightLeft - height[l]
            else:
                # rightMax is smaller
                r -= 1
                maxHeightRight = max(maxHeightRight, height[r])
                waterQty += maxHeightRight - height[r]
        
        return waterQty
                




        

        