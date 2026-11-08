# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find the middle of the LL - will be where slow lands.
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the RHS of the LL from mid onwards
        curr = slow
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        rightSideHead = prev

        # interleave/zip together the two LLs
        left, right = head,rightSideHead

        while left and right:
            tmpleft = left.next
            tmpright = right.next

            left.next = right
            right.next = tmpleft

            left = tmpleft
            right = tmpright
        
        




        