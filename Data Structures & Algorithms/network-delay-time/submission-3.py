import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTimeTo = {} # dict of node label and min times to int
        adjList = {} # mapping of node to its neighbours, as array of neighbour/time tuples

        for src, dst, dur in times:
            if not src in adjList:
                adjList[src] = []

            adjList[src].append((dst, dur))

        sendsrc = k
        minTimeForAllNodes = 0 # the min time for all nodes will be the longest time we find.

        heap = [(0, sendsrc)] # q has tups of travel time, node, so it sorts on time.  Start with src node.
        heapq.heapify(heap)
        
        # BFS
        while heap:
            timeToCurr, curr = heapq.heappop(heap)

            # min heap will always pop smallest first. if we are doing BFS then once we pop a node we can assume its the smallest in the graph.
            if not curr in minTimeTo:
                minTimeTo[curr] = timeToCurr

                minTimeForAllNodes = timeToCurr # this will be the last one from the minheap

                neigh = adjList.get(curr, [])
                for  targ, _time in neigh:
                    if not targ in minTimeTo:
                        # each neighbours time must include time to its parent!
                        heapq.heappush(heap, (timeToCurr + _time, targ))
            
        return minTimeForAllNodes if len(minTimeTo) == n else -1
                
            

            

        

