import heapq
class Solution:    
    # using Min heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        minheap = []
        heapq.heapify(minheap)

        merged = ListNode()
        curr = merged

        # counter for tiebreaker so that heap pop 
        # and push can "rank" nodes that have equal values.
        # We push tuple on to minheap because the comparisons run left to right
        # so we want the val to be first comparitor, THEN the counter if the vals are the same
        counter = 0 
        for ll in lists:
            if ll:
                heapq.heappush(minheap, (ll.val, counter, ll))
                counter+=1
        
        while minheap:
            val, _, smallest = heapq.heappop(minheap)
            if smallest.next:
                heapq.heappush(minheap,( smallest.next.val, counter, smallest.next))
                counter += 1    
            
            curr.next = smallest
            curr = curr.next
        
        # return next because merged first node is dummy
        return merged.next


    # # recursively merge lists. But can have excessive space complexity.
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if len(lists) == 0: return None

    #     def mergeSortedLists(list1, list2):
    #         if not list1: return list2
    #         if not list2: return list1

    #         if list1.val <= list2.val:
    #             list1.next = mergeSortedLists(list1.next, list2)
    #             return list1
    #         else:
    #             list2.next = mergeSortedLists(list1, list2.next)
    #             return list2
            

    #     merged = None
    #     for i in range(1, len(lists)):
    #         merged = mergeSortedLists(lists[i-1], lists[i])
    #         lists[i] = merged

    #     return lists[-1]


    # # recursively merge lists. But can have excessive space complexity.
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if len(lists) == 0: return None

    #     def mergeSortedLists(list1, list2):
    #         if not list1: return list2
    #         if not list2: return list1

    #         if list1.val <= list2.val:
    #             list1.next = mergeSortedLists(list1.next, list2)
    #             return list1
    #         else:
    #             list2.next = mergeSortedLists(list1, list2.next)
    #             return list2
            

    #     merged = None
    #     for i in range(1, len(lists)):
    #         merged = mergeSortedLists(lists[i-1], lists[i])
    #         lists[i] = merged

    #     return lists[-1]