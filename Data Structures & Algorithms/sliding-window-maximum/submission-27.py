import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maxheap = []

        res = []
        for right in range(len(nums)):
            # store  val (as sorting key) and its index
            heapq.heappush(maxheap, [-1 * nums[right], right])

            if right - left + 1 >= k:
                while maxheap[0][1] < left:
                    heapq.heappop(maxheap)
                
                maxval = maxheap[0][0]
                res.append(-1 * maxval)

                left += 1 

        return res



