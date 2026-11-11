# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        maxheightdiff = -1

        def dfs(node):
            """
            build height bottom up.  So leaf node returns 0.
            and each call to dfs() adds 1 + to the returned result to increment height.
            Get the height of the tree by getting max of left and right sub trees
            get the diff between the two left and right heights
            update global max
            the dfs function MUST return the height of the subtree at this node, so returns max(left, right)
            """
            if not node: return 0
            nonlocal maxheightdiff
            
            left = 1 + dfs(node.left)
            right = 1+ dfs(node.right)

            heightDiff = abs(left - right)
            maxheightdiff = max(maxheightdiff, heightDiff)
            
            return max(left, right)

        dfs(root)
        return maxheightdiff <=1