from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTimes = {}

        # build adjacency list -> neighbour vertices
        adj = defaultdict(list)
        
        for s, d, t in times:
            adj[s].append((d, t))


        src = k
        timeForAll = 0
        heap =  [(0, src)] # tuple of (time, destination), calculated from src starting point
        heapq.heapify(heap)

        while heap:
            time, node = heapq.heappop(heap)

            # minHeap will always give min values so the earlier one is the shortest.
            if not node in minTimes:
                minTimes[node] = time
            
                timeForAll = time #eventually this will hold the longest time, when heap is empty
            
                # get neighbours
                neighbours = adj[node]

                for nd, nt in neighbours:
                    if not nd in minTimes:
                        heapq.heappush(heap, (time + nt, nd )) # time of prev node + current node
        
        # min time for ALL is max time
        return timeForAll if len(minTimes.keys()) == n else -1


    

         