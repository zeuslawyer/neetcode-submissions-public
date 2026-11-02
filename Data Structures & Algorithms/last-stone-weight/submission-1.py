import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        maxheap = []
        heapq.heapify(maxheap)

        for s in stones:
            # negative numbers so that its a max heap
            heapq.heappush(maxheap, -s) 
        

        while len(maxheap) > 1:
            first, second = heapq.heappop(maxheap), heapq.heappop(maxheap) 
            if first == second:
                # both stones destroyed
                continue
            else:
                newstone = abs(first-second)
                heapq.heappush(maxheap,  -newstone)
            
        
        return 0 if len(maxheap)== 0 else -1 * heapq.heappop(maxheap)



        