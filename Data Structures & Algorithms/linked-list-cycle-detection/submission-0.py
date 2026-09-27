# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tracker = {}

        curr = head
        index = 0

        while curr:
            lastIndex = tracker.get(curr.val)
            # found it
            if lastIndex: return True


            tracker[curr.val] = index
            index+=1

            curr = curr.next

        return False 