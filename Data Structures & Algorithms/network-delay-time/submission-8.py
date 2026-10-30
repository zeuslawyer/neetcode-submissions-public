import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}

        for src, dst, t in times:
            adj[src].append((t, dst))

        # min time is constrained by the max time - the time it takes until the LAST node in the network receives the signal.

        start = k
        minTimeTo = {} # min time from K to all others
        minheap = [(0, start)] # tuple of distance to itself from the start
        heapq.heapify(minheap)

        longestTime = 0 # since the min time for ALL N nodes is the time the LAST node receives it....

        while minheap:
            time, node = heapq.heappop(minheap)
            if not node in minTimeTo:
                minTimeTo[node] = time
                # longestTime = max(longestTime, time) # we dont need this as MIN heap means it will always be increase
                longestTime = time
                for ncost, nnode in adj[node]:
                    heapq.heappush(minheap, (ncost + time, nnode))

        if len(minTimeTo) == n: 
            return longestTime
        else:
            return -1
