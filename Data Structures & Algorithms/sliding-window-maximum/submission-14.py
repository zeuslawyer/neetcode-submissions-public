from collections import deque

# Using deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # store indices as that helps track whether a num is inside window
        res = []
        left = 0
        for right in range(len(nums)):
            num = nums[right]

            # always check against back of the q to pop all nums smaller than num
            while q and num >= nums[q[-1]]:
                q.pop()
            # then append. So back of queue is always the current maximum.
            q.append(right)

            # now check front of q. If the index is outside window, pop
            if q[0] < left:
                q.popleft()

            # if right - left + 1 < k:
            #     continue            # window not full yet

            # res.append(nums[q[0]])
            # left += 1

            # if the window size is k then append the max, which is front of q. Also keep sliding the left to maintain window size.
            if right - left + 1 == k:
                res.append(nums[q[0]])
                left += 1

        return res