# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# BFS level order
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        count = 0
        q = deque()
        q.append((root, root.val))

        while q:
            for i in range(len(q)):
                node, maxfromparents = q.popleft()

                if node.val >= maxfromparents:
                    count += 1
                    maxfromparents = max(maxfromparents, node.val)
                
                if node.left: q.append((node.left, maxfromparents))
                if node.right: q.append((node.right, maxfromparents))


            
        return count




        