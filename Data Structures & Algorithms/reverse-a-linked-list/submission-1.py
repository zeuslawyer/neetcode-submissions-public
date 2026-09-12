# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # iteration
        curr, prev = head, None

        while curr: 
           next = curr.next
           curr.next=prev
           prev = curr
           curr=next
        
        # the while loop exits only when curr is None, so head will be prev
        return prev 
