# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        count = 0
        def dfs(node, maxsofar):
            if not node: return

            if node.val >= maxsofar:
                nonlocal count
                count+=1
                maxsofar = node.val
            
            dfs(node.left, maxsofar)
            dfs(node.right, maxsofar)


        dfs(root, root.val)

        return count
        