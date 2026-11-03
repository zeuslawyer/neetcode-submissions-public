# Use two heaps to store the values. LHS of the array is in the maxHeap
# and the RHS of the array in the min heap. 
# All vals in maxheap must be <= minheap. 
# we try and ensure that the heap sizes are within +- 1 of each other.

import heapq
class MedianFinder:
    def __init__(self):
        self.maxHeapSmallVals = []
        self.minheapBigVals = []
        

    def addNum(self, num: int) -> None:
        # we always add to the smaller heap and rebalance heaps later.
        maxHeap = self.maxHeapSmallVals
        minHeap = self.minheapBigVals
        heapq.heappush(maxHeap, -1 * num)

        # check that the LHS doesnt have a number thats bigger than RHS
        # since its a heap the maxheaps top has the largest number in the heap
        if minHeap and (-1 * maxHeap[0]) > minHeap[0]:
            val = -1 * heapq.heappop(maxHeap)
            heapq.heappush(minHeap, val)
        
        # balance sizes
        if len(maxHeap) - len(minHeap) > 1:
            val = -1 * heapq.heappop(maxHeap)
            heapq.heappush(minHeap, val)
        
        if len(minHeap) - len(maxHeap) > 1:
            val =  heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -1 * val)


    def findMedian(self) -> float:
        # if even length then we take avg of (mid1 and mid2) else we get the longer of the two heaps
        maxHeap = self.maxHeapSmallVals
        minHeap = self.minheapBigVals
        if len(maxHeap) > len(minHeap):
            return -1 * maxHeap[0]
        if len(minHeap) > len(maxHeap):
            return minHeap[0]
        
        # they're equal
        return (minHeap[0] + -1 * maxHeap[0]) / 2
        
        