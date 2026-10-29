# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point using slow + fast pointers.
        # then reverse the second half of the list
        # then interleave the two LLs.

        # find mid point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # RHS of LL starts with slow
        rightSideStart = slow
        curr = rightSideStart
        prev = None
        # reverse linked list
        while curr:
            # store downstream
            tmp = curr.next
            # flip pointers on curr
            curr.next = prev
            prev = curr
            curr = tmp
        
        # update where the right side of list starts - used to be the tail of the RHS
        rightSideStart = prev
        
        # interleave/merge
        left = head
        right = rightSideStart
        while right and right.next:
            tmpleft = left.next
            tmpright = right.next
            
            # reconnect
            left.next = right
            right.next = tmpleft
            
            # move pointers
            left = tmpleft
            right = tmpright
