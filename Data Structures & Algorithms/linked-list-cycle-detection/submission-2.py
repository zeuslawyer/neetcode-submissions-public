# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # using id of object in memory
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tracker = set()

        curr = head

        while curr:
            if id(curr) in tracker: return True
            
            tracker.add(id(curr))
            curr=curr.next  

        return False 