import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i:[] for i in range(n)}
        for i, (n1, n2) in enumerate(edges):
            adj[n1].append((succProb[i], n2))
            adj[n2].append((succProb[i], n1))
        
        fromStartTo = {}

        maxheap = [(-1.0, start_node)] # initial tuple - probability, edge. But since we want this node to lead, we give it -1
        heapq.heapify(maxheap)

        while maxheap:
            currprob, currnode = heapq.heappop(maxheap)

            if currnode == end_node:
                return -1 * currprob
                

            if currnode not in fromStartTo:
                fromStartTo[currnode] = -1 * currprob

                for nprob, dest in adj[currnode]:
                    # note nprob from the adj array is +ve not negative, so this produces a -ve prob
                    heapq.heappush(maxheap,  (currprob * nprob, dest))
        
        
        return 0



        