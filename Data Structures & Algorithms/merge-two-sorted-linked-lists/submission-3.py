# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1: return list2
        if not list2: return list1

        # setup merged LL with dummy head
        head = ListNode()
        # pointer to current node
        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                # attach the smaller value to the merged list
                curr.next = list1
                # snipt off head of the list
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2. next
            
            # update pointer
            curr = curr.next
        
        # List1 or list2 are empty. So attach the other one which is sorted anyway.
        curr.next = list1 or list2

        # head is dummy so merged list starts with next.
        return head.next


        