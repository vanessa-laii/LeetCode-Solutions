# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # can the result be a new list
        # does the sorting need to be stable?
        # whats the maximum lengths of the lists
        # ascending order

        # min heap
        # put the head of every list in the heap, as you tae=ke, push next element into heap
        # we need a tie breaker so take l
        heap = []
        for l in range(len(lists)):
            head = lists[l]
            if head:
                heapq.heappush(heap, (head.val, l, head))
        
        # now keep poping from the heap and into the res LL
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, l, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, l, node))
        
        return dummy.next

        