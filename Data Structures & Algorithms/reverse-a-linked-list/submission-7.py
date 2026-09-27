# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return None
        if not head.next: return head

        prev = None

        def reverse(curr: Optional[ListNode], prev:  Optional[ListNode]):

            if not curr: return prev # prev is the last node so its the new head.

            # flip/update only this node
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp


            return reverse(curr, prev)
        
        return reverse(head, prev)


            