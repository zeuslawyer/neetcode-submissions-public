import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}  # adj map

        # add time, dst tuples to adj map
        for src, dst, t in times:
            adj[src].append((t, dst))
        
        # track min times from K to each other node
        minTimeTo = {  }
        
        # push time taken from k to itself and k as starting node
        minheap = [(0, k)]
    
        # min time for all nodes is constrained by the LAST node to get signal
        mintime = 0

        while minheap:
            time, node = heapq.heappop(minheap)
            
            if node not in minTimeTo:
                
                minTimeTo[node] = time
                 # the last node to pop will have the accumulated shortest path time 
            # which is the min time for ALL n nodes to receive signal.
                mintime = time

                for nt, nn in adj[node]:
                    if nn not in minTimeTo:
                        # accumulate time to predecessor node when computing time to neighbour
                        heapq.heappush(minheap, (time + nt, nn))
                
        
        return mintime if len(minTimeTo) == n else -1
