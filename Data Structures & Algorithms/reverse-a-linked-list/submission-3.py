# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # # iteration
        # curr, prev = head, None

        # while curr: 
        #    next = curr.next
        #    curr.next=prev
        #    prev = curr
        #    curr=next
        
        # # the while loop exits only when curr is None, so head will be prev
        # return prev 


        # recursion
        return self.helper(head, None)
    

    def helper(self, curr, prev) -> ListNode:
        if curr == None:
            return prev

        next = curr.next
        # flip pointer to point backwards
        curr.next = prev
        return self.helper(next, curr)

        # OR 
        # new_curr = curr.next
        # new_prev = curr
        # # flip pointer backwards
        # curr.next = prev
        # return self.helper(new_curr, new_prev)

        
        





            
        
        
        

