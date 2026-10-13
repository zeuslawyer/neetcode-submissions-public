

class MinHeap:
    
    def __init__(self):
        self.heap=[]
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)


    def pop(self) -> int:
            if len(self.heap) == 0: return -1
            # swap top and bottom of heap
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            smallest = self.heap.pop()
            self._pushdown(0)
            return smallest
        

    def top(self) -> int:
        return self.heap[0] if len(self.heap) > 0 else -1
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums.copy()
        parentIdx = (len(nums)-1-1)//2 

        for i in range(parentIdx, -1, -1):
            self._pushdown(i)



    def _bubble_up(self, index) -> None:
        currIdx = index

        while currIdx >0:
            parentIdx = (currIdx-1)//2
            if self.heap[parentIdx] > self.heap[currIdx]:
                self.heap[parentIdx], self.heap[currIdx] = self.heap[currIdx], self.heap[parentIdx]
                currIdx = parentIdx
            else:
                break
    
    def _pushdown(self, idx) -> None:
        while idx < len(self.heap):
            leftIdx, rightIdx = (2*idx) + 1, (2*idx) + 2
            
            # find which element to swap with - the lowest of the two children (since min heap)
            swapIdx = leftIdx
            if rightIdx < len(self.heap)  and self.heap[rightIdx] < self.heap[leftIdx]:
                swapIdx = rightIdx

            # check if swap is needed
            if swapIdx < len(self.heap) and self.heap[swapIdx] < self.heap[idx]:
                self.heap[idx], self.heap[swapIdx] = self.heap[swapIdx],  self.heap[idx]
                idx = swapIdx
            else:
                # no swaps needed. resting place found.
                break

            




        
        
        
            


        
        
        
        