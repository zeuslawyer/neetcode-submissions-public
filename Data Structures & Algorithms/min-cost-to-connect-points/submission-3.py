from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)
    
        # adj list has mapping of node index to its neighbour node index, with associated cost
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]  
                cost = abs(xi-xj) + abs(yi-yj)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        
        minheap = [(0,0)] # tuple of cost and starting node. We can start from ANY. and cost ALWAYS defaults to 0 in prims.
        heapq.heapify(minheap)
        visited = set()
        mincost = 0

        while len(visited) < N:
            cost, idx = heapq.heappop(minheap)

            if idx not in visited:    
                visited.add(idx)
                mincost += cost

                for nei in adj[idx]:
                    ncost, nidx = nei
                    if nidx not in visited:
                        heapq.heappush(minheap, (nei))
        
        return mincost