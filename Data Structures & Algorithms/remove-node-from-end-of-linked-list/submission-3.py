# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer with fixed gap. F = S + N + 1.  Therefore when F is at len 
        # F - N - 1 is the node just BEFORE the one to be snipped.  
        # so S = F - N - 1 ==> S + N + 1 == F

        # for situations where N = len of LL, (i.e removing head of LL) then we need an extra dummy or the F = S + N +1 logic crashes as its out of bounds.

        dummy = ListNode(val=0, next = head)

        slow = fast = dummy
        
        # F has to be N+1 ahead of slow
        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next # maintain fixed distance from slow - i.e N+1. 
        
        # rewire slow which is at N-1 in the LL
        slow.next = slow.next.next

        return dummy.next


    