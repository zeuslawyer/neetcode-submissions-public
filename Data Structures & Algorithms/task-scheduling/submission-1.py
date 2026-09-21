from _heapq import heappop
from calendar import c
from collections import deque, Counter, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the frequence of each task
        counter = defaultdict(int)  

        for task in tasks:
            counter[task] += 1
        
        # Task Priority Queue. This is where tasks get pulled from.
        maxheap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxheap)

        # cool down queue. This is where tasks wait to be put back into priority queue.
        q = deque()

        cycletime = 0

        while maxheap or q:
            # we are using up one CPU cycle.
            cycletime += 1

            if maxheap:
                # process the task from the priority queue
                count = heapq.heappop(maxheap)
                # decrement count since task has just been done
                count += 1 # count is negative so add
                
                # Goes into cool down q, with a timestamp for when its NEXT due
                # count is -ve so get abs.
                if abs(count) >0: 
                    cooldown_end = cycletime + n
                    q.append([count, cooldown_end])

            
            # Pull from the cooldown queue 
            if q:
                cooldown_end = q[0][1]
                if cycletime == cooldown_end:
                    cnt, _ = q.popleft()
                    heapq.heappush(maxheap, cnt)

        return cycletime
