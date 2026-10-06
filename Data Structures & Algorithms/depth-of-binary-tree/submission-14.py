# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dive(node, depth):
            if not node: return depth
            depth +=1
            left = dive(node.left, depth)
            right = dive(node.right, depth)
            return max(left, right)

        return dive(root, 0)
        

      

            



        