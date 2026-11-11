# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS   
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxsofar):
            nonlocal count 

            if not node:
                return

            if node.val >= maxsofar:
                count += 1
                maxsofar = node.val
            
            dfs(node.left, maxsofar)
            dfs(node.right, maxsofar)
        
        dfs(root, root.val)

        return count

            


      
        





