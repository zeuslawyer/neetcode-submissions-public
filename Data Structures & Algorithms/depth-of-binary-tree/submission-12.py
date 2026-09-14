# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS with recursion

        return self.traverse(root, 0)
    

    def traverse(self, node, depth) -> int:
        if not node:
            return depth

        depth += 1

        left = self.traverse(node.left, depth)
        right = self.traverse(node.right, depth)

        return max(left, right)  