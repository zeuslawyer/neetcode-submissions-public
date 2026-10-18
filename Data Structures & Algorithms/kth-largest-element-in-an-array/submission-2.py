import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0: return 0
        
        heap = [-num for num in nums]
        heapq.heapify(heap)

        popped = []
        for i in range(k):
            popped.append(heapq.heappop(heap))
        
        return popped[-1] * -1
        
