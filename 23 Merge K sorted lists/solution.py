# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # push into a min heap to sort the nodes
        # rebuild heap into a LL
        heap = []
        for l in range(len(lists)):
            head = lists[l]
            if head:
                # the index l acts as a tie breaker for the heap
                heapq.heappush(heap, (head.val, l, head))
        
        dummy = ListNode(0)
        curr = dummy 

        while heap:
            val, index, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            # push in the next node in the list 
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, index, node))
        
        return dummy.next





        
        