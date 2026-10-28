"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# BFS
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        cloneOf = {} # since its UNDIRECTED graph , we can expect cycles. Therefore stop condition is NOT empty neighbour list.
        
        q = deque()
        q.append(node)
        cloneOf[node] = Node(node.val)
        while q:
            popped = q.popleft()


            for nei in popped.neighbors:
                if nei in cloneOf: 
                    cloneOf[popped].neighbors.append(cloneOf[nei])
                    continue
                # else 
                #clone and append nei
                cloneOf[nei] = Node(nei.val)
                q.append(nei)
                # attach clone nei to the clone of current popped
                cloneOf[popped].neighbors.append(cloneOf[nei])


        return cloneOf[node]


            