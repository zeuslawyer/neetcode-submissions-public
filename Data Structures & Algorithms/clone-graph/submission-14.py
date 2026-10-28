"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        # since its UNDIRECTED graph , we can expect cycles. Therefore stop condition is NOT empty neighbour list.
        cloneOf = {}
        
        def cloneNode(node):
            if node in cloneOf: return cloneOf[node]
            
            newNode = Node(node.val, [])
            cloneOf[node] = newNode
            
            for nei in node.neighbors:
                newNode.neighbors.append(cloneNode(nei))
            
            return newNode

        return cloneNode(node)


            