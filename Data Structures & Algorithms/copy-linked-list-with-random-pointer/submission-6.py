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
        # two passes. One to clone and store in hashmap. the next to wire up pointers.
        cloneOf = {}
        
        # first pass
        curr = head
        while curr:
            cloneOf[curr] = Node(curr.val)
            curr = curr.next
        
        # second pass
        curr = head
        while curr:
            clone = cloneOf[curr]
            clone.next = cloneOf.get(curr.next, None)
            clone.random = cloneOf.get(curr.random, None)
            
            curr = curr.next

        return cloneOf[head] if head else None
