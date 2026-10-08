# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Longest path ("triangle") is = longest *branch* in left subtree + current node + longest
        *branch*  in right subtree.

        """

        if not root: return 0
    
        res = root.val

        def longestBranchInTree(node):
            """
            1. Calculate the single longest branch in either subtrees of a given node.
            2. All the while, update the longest triangle (longest path) seen SO FAR.
            """
            if not node: return 0

            leftMax = longestBranchInTree(node.left)
            rightMax = longestBranchInTree(node.right)

            if leftMax < 0: leftMax = 0
            if rightMax < 0: rightMax = 0


            nonlocal res
            res = max(res, leftMax + node.val + rightMax )

            return node.val + max(leftMax, rightMax)
        
        longestBranchInTree(root)
        return res