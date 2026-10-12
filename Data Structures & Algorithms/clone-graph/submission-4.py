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

        cloneOf = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr not in cloneOf:
                cloneOf[curr] = Node(curr.val)

            for nbor in curr.neighbors:
                if nbor not in cloneOf:
                    q.append(nbor)
                    cloneOf[nbor] = Node(nbor.val)

                cloneOf[curr].neighbors.append(cloneOf[nbor])

        return cloneOf[node]
                





        