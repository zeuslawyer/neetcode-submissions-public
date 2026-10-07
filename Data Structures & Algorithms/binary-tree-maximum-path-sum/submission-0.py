# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        res = root.val

        # find the max sum of nodes that go via current node ("Triangle length".  this is returned value as well)
        # also find max path down each subtree
        
        def getMaxBranchLength(node):
            """
            returns the max branch
            """
            if not node: return 0

            nonlocal res

            leftmax = getMaxBranchLength(node.left)
            rightmax = getMaxBranchLength(node.right)

            # discard -ve values
            if leftmax < 0: leftmax = 0
            if rightmax < 0: rightmax = 0

            # store max "triange" length
            res = max(res, leftmax + node.val + rightmax)

            return node.val + max(leftmax, rightmax)
        

        getMaxBranchLength(root)
        return res

            
