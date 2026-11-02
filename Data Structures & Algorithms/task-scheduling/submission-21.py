from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        
        maxheap = [(-count, task) for task, count in counts.items()]
        heapq.heapify(maxheap)

        # cooldown q
        q = deque() # enqueue the remaining counts, next cycle time and task

        time = 0 # cycle time
        while maxheap or q:
            time += 1 # MARK CYCLE time no matter what happens next

            # only items pulled off the maxheap reduce the counts.
            if maxheap:
                count, task = heapq.heappop(maxheap)

                # decrement by adding because count is -ve number
                count += 1 

                # enqueue if we're NOT done with this task
                if count != 0:
                    next_time = time + n
                    q.append((count, next_time, task ))

            # things that have cooled down get pushed into the heap for processing. This happens regardless of whether there is a maxheap
            if q:
                next_time = q[0][1]    
                if time >= next_time:
                    count, next_time, task = q.popleft()
                    heapq.heappush(maxheap, (count, task))

        return time