import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums): return []

        res = []
        left = 0
        maxheap =  []
        for right in range(len(nums)):
            # store val AND index
            heapq.heappush(maxheap, (-1*nums[right], right))
            
            # window too small. keep expanding.
            if (right-left+1) < k:
                continue
            
            # window size achieved. 
            # start checking if val at top of heap is outside window
            while  maxheap[0][1] < left:
                heapq.heappop(maxheap)
            
            # Start pushing and popping from maxheap
            maxInWindow = -1 * maxheap[0][0]
            res.append(maxInWindow)
            left +=1
            # no need to update right as the loop will handle it and update window size.
        return res                


        