# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return None
        
        # 1 find the middle of LL
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the middle.
        # reverse the RHS LL
        curr = slow
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        reversedHead = prev

        # interleave/merge the two LLs
        left, right = head, reversedHead

        # once the shorter one runs out all the wiring is complete
        while left and right:
            tmpleft, tmpright = left.next, right.next
            left.next = right
            right.next = tmpleft

            left = tmpleft
            right = tmpright
        

        