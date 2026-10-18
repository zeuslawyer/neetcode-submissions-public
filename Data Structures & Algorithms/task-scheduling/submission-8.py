from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxheap = [-num for num in counts.values()]
        heapq.heapify(maxheap)

        cycle_time = 0
        cooldown_q = deque() # tuple of remaining count, cooldown end time

        while maxheap or cooldown_q:
            cycle_time +=1

            # if heap empty, move time forward to next time as per head of queue
            if not maxheap:
                cycle_time = cooldown_q[0][1]
            else:
                count = heapq.heappop(maxheap)
                # decrement the task's counts
                count +=1
                
                # if this task has count remaining, append it to queue along with cooldown time
                if abs(count) > 0:
                    next_cycle_time = n + cycle_time
                    cooldown_q.append((count, next_cycle_time))
            
            if cooldown_q and cycle_time == cooldown_q[0][1]:
                count, time = cooldown_q.popleft()
                heapq.heappush(maxheap, count)

        
        return cycle_time


