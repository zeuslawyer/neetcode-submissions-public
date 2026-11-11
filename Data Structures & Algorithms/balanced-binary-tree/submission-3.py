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
            Get the height of the tree by getting max of left and right sub trees.
            Height at current level becomes 1 + max(left, right). Add 1 later.
            To calculate balance, get the diff between the two left and right heights
            update global max
            the dfs function MUST return the height of the subtree at this node, 
            so returns max(left, right)
            """
            if not node: return 0
            nonlocal maxheightdiff
            
            # dont add 1 here.  because the height of a tree is determined by the MAX of left and right.
            # so add 1 there.
            left =  dfs(node.left)
            right = dfs(node.right)

            heightDiff = abs(left - right)
            maxheightdiff = max(maxheightdiff, heightDiff)
            
            # add 1 here 
            return 1 + max(left, right)

        dfs(root)
        return maxheightdiff <=1