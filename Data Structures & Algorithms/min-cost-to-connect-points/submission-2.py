import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Each point[] is a single node in graph.
        # idx is the label for that node, and its val is the (x,y)point
        # distance between two points is the "cost". 
        
        # build adj list
        N = len(points)
        adj = {i:[]for i in range(N)}

        # build distances for each node
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                cost = abs(xi-xj) + abs(yi - yj)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
            

        minheap = [(0,0)] # tuple(dist/cost, node id), keyed by dist.
        heapq.heapify(minheap)
        visited = set()
        totalcost = 0

        # MST only complete when all nodes are visited. So...
        while len(visited) <  N:
            cost, node = heapq.heappop(minheap)
            if node not in visited:
                visited.add(node)
                totalcost += cost
                for ncost, n in adj[node]:
                    if n not in visited:
                        heapq.heappush(minheap,(ncost, n))
            
        return totalcost




            
        
            

        