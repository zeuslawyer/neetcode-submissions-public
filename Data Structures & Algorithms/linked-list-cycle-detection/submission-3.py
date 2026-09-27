# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # track the object not just the value as 
        # repeat values can happen without a cycle
        tracker = set()

        curr = head

        while curr:
            if curr in tracker: return True
            
            tracker.add(curr)
            curr=curr.next  

        return False