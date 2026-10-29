# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # new sorted list is allowed
        # start with a dummy starting ListNode

        head = ListNode(val = -1)

        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        # either list 1 or list 2 are now empty
        curr.next = list1 or list2
        
        return head.next

