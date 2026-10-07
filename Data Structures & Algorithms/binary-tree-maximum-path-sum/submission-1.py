# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # calculate "triangle" of max value of path THROUGH current node.
        # this triangle path sum is final returned value too.
        # for each node the triangle is  highest left branch + highest right branch.

        res = root.val

        def maxBranchLength(node):
            if not node: return 0

            # to compute longest branch we FIRST need longest branch from each subtree and THEN we add that to the node.  So we need POST ORDER as information comes from sub trees (below)
            leftmax = maxBranchLength(node.left)
            rightmax = maxBranchLength(node.right)

            # discard negative branch sums because they always reduce the maxBranchLength
            if leftmax < 0: leftmax = 0
            if rightmax < 0:  rightmax = 0

            # update the result with highest triangle sum
            nonlocal res
            res = max(res, leftmax + node.val + rightmax)

            return node.val + max(leftmax, rightmax)

        maxBranchLength(root)
        return res