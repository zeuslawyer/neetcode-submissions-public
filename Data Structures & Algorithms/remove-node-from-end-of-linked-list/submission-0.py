# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
    
        count = 0
        curr = head

        while curr:
            count +=1
            curr = curr.next
        
        target = count - n
    
        if target == 0:
            new_head = head.next
            head = None
            return new_head

        pointer = head
        for i in range(target-1):
            pointer = pointer.next
        
        pointer.next = pointer.next.next

        return head






        