import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total_time = 0
        if not tasks: return total_time

        counter = Counter(tasks)

        # Max Heapify the task counts
        maxheap = [-count for count in counter.values()]
        heapq.heapify(maxheap)

        cooldown_q = deque() # tuple of (remainng count, next non idle time)

        while maxheap or cooldown_q:
            total_time += 1

            # if all tasks are in cooldown
            if not maxheap:
                total_time = cooldown_q[0][1]
            else: 
                 # track cycle time and decrement remaining runs of this task
                 # is negative number so decrement by addition
                taskcount = heapq.heappop(maxheap) + 1

                if abs(taskcount) > 0:
                    required_idle_time = n + total_time
                    cooldown_q.append((taskcount, required_idle_time))

            # check head of queue to see if their idle time is done
            if cooldown_q and total_time == cooldown_q[0][1]:
                next_task_count = cooldown_q.popleft()[0]
                heapq.heappush(maxheap, next_task_count)
        
        return total_time
