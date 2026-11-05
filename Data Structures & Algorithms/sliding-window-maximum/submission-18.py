from collections import deque

# use a downward Monotonic queue to make O(1) pops and appends.
# the monotonic q ONLY holds Indexes.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        q = deque()
        
        res = []
        for right in range(len(nums)):
            num = nums[right]

            # since its down Monotonic, ensure that smaller numbers are popped
            while q and nums[q[-1]] < num:
                popped = q.pop()
            
            # then append current ***INDEX***.
            q.append(right)

            # compare **INDEX** at head of q to make sure its not stale or less than window start.
            if q[0] < left:
                q.popleft()

            while right - left + 1 == k:
                # its a monotonic queue so head of q is largest
                res.append(nums[q[0]])
                left +=1 
        
        return res

            




        