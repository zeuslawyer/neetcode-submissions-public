class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxHeightL, maxHeightR = height[l], height[r]

        water = 0

        while l < r:
            # only move the smaller of the two max heights. Because that sets the max amount of water height 
            if maxHeightL < maxHeightR:
                l+=1
                # capture the new height
                maxHeightL = max(maxHeightL, height[l])
                # calculate vertical height of current index (i.e. l)
                water += maxHeightL - height[l]
            else:
                r -= 1
                maxHeightR = max(maxHeightR, height[r])
                water += maxHeightR - height[r]
            
        return water
            
            

        