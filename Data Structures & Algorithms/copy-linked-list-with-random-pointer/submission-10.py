"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        # use two passes. One clones, the next wires up pointers.
        copyOf = {}

        curr = head
        while curr:
            copyOf[curr] = Node(curr.val)
            curr = curr.next
        
        # second passes
        curr = head
        while curr:
            copy = copyOf[curr]
            copy.next = copyOf[curr.next] if curr.next else None
            copy.random = copyOf[curr.random] if curr.random else None

            curr = curr.next
        
        return copyOf[head]