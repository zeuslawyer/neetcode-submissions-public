# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Re order IN PLACE without using extra memory

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None

        # find the approx mid to split the linked list into 2
        # use slow pointer and fast pointer to track mid point and end of LL, respectively
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            # fast always skips ahead by 2
            fast = fast.next.next
        
        # RHS starts at slow's next node
        RHList = slow.next
        # terminate the LH list
        slow.next = None

        # We need to reverse the RHS LL because effectively it gets inserted into the new list in reverse order
        curr, prev = RHList, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # new head of reversed list used to be the last node , which is now prev
        RHList = prev
        # merge LH list and RH list
        LHList = head
        
        # len of RH list is <= LH list so use that as iteration
        while RHList:
            # severing connections in both lists
            LHTmp, RHtmp = LHList.next, RHList.next
            LHList.next = RHList
            RHList.next=LHTmp
            LHList = LHTmp
            RHList = RHtmp

            
            
            






        



        
        