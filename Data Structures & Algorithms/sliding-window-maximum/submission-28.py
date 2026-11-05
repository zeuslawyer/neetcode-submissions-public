import heapq

# max heap.  store index and value and key on the index. so if index is < left pointer
# it means the window in the heap needs shortening.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maxheap = []

        res = []
        for right in range(len(nums)):
            # store  val (as sorting key) and its index
            heapq.heappush(maxheap, [-1 * nums[right], right])

            if right - left + 1 >= k:

                # check the index and compare to left ptr
                while maxheap[0][1] < left:
                    heapq.heappop(maxheap)
                
                maxval = maxheap[0][0]
                res.append(-1 * maxval)

                left += 1 

        return res



