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
            if popped not in cloneOf:
                cloneOf[popped] = Node(popped.val)

            for nei in popped.neighbors:
                if nei not in cloneOf:
                    # enqueue only if NOT already processed
                    q.append(nei)
                    # mark as visited by cloning
                    cloneOf[nei] = Node(nei.val)
                
                # attach the cloned nei to clone of popped.
                # it either existed or was just created above.

                cloneOf[popped].neighbors.append(cloneOf[nei])


        return cloneOf[node]


            