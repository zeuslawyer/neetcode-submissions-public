from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {n:[] for n in range(N)}

        for i in range(N):
            xi,  yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                dist = abs(xi-xj) + abs(yi-yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visitedNodes = set()
        minheap = [(0, 0)] # tuplle of distance, starting node
        heapq.heapify(minheap)

        mincost = 0

        while len(visitedNodes) < N:
            cost, n = heapq.heappop(minheap)
            if n not in visitedNodes:
                visitedNodes.add(n)
                mincost += cost

                for c, node in adj[n]:
                    if node not in visitedNodes:
                        # MST/Prims so no accum of cost
                        heapq.heappush(minheap, (c, node))
        
        return mincost





        

        
            
        