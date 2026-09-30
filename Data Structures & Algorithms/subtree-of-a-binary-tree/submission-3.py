# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def compareTrees(tree1, tree2) -> bool:
            stack = [(tree1, tree2)]
            
            # DFS to compare
            while stack:
                t1, t2 = stack.pop()
                if not t1 and not t2: continue

                if not t1 or not t2: return False
                if t1.val != t2.val:  return False

                # the nodes are equal
                stack.append((t1.left, t2.left))
                stack.append((t1.right, t2.right))

            return True
        
        q = deque([root])


        # BFS to navigate both the tree to start comparing each node with the subroot
        while q:
            node = q.popleft()
            if node and node.val == subRoot.val:
                same = compareTrees(node, subRoot)
                if same: return True
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
                
        return False
