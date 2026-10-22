# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []

        # push all LL nodes into list
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        # iterate and apply the formulate for twins
        n = len(nodes)
        maxTwinSum = 0

        for i in range(n):
            twinIdx = n-1-i

            if i < twinIdx:
                sum = nodes[i].val + nodes[twinIdx].val
                maxTwinSum = max(maxTwinSum, sum)
            
        return maxTwinSum
        