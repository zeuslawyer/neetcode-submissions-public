from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minheap = []
        heapq.heapify(minheap)

        # create minheap of size k
        for num in freq:
            heapq.heappush(minheap, (freq[num], num))
            if len(minheap) > k:
                heapq.heappop(minheap)
            
        # assemble k most frequent
        res = []
        for i in range(k):
            freq, num = heapq.heappop(minheap)
            res.append(num)
    
        return res





        