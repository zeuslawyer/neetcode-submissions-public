# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)

        while q:
            # level = []
            rightmost = None
            for i in range(len(q)):
                curr = q.popleft()
                # level.append(curr.val)
                rightmost = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            # right_most = level.pop()
            # res.append(right_most)
            res.append(rightmost)
        
        return res
        

        