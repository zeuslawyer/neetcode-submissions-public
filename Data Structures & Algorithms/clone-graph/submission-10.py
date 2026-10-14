"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

# BFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        cloneOf= {}
        cloneOf[node] = Node(node.val)

        q = deque([node])

        while q:
            curr = q.popleft()
            if curr not in cloneOf:
                # clone the current node
                cloneOf[curr] = Node(curr.val)

            # enqueue current's neighbours
            for n in curr.neighbors:
                if n not in cloneOf:
                    cloneOf[n] = Node(n.val)
                    q.append(n)

                #  attach neighbour clones to the clone
                cloneOf[curr].neighbors.append(cloneOf[n])
        
        
        return cloneOf[node]
            
