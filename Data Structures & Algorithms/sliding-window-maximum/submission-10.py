from collections import deque

# Using deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # store indices as that helps track whether a num is inside window
        res = []
        for i in range(len(nums)):
            num = nums[i]
            
            # back: check back of q. If that num is smaller than num then replace it with num as we are always looking for largest num in window.
            # while loop replaces ALL nums that are < num at back of q.
            while q and nums[q[-1]] <= num:  
                q.pop() # i.e. popright!
            
            # append the current index for num
            q.append(i)

            # check front of queue. If index < left then evict it.
            if i + 1 - k > q[0] :  
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])

        return res