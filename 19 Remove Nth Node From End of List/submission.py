# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # method 2 - two pointers
        dummy = ListNode(0, head)
        curr = dummy
        
        # create the gap of n between 2 pointers
        for i in range(n):
            head = head.next
        
        # move left and right to the end
        while head:
            head = head.next
            curr = curr.next
        
        # mod pointers to delete node - skip the one after left
        curr.next = curr.next.next

        return dummy.next
        
        



        # modifying the end of a linked list 
        # use a stack to store the nodes of the entier linked list
            # count the length of the linked list 
        # stack = []
        # curr = head
        # length = 0
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next
        #     length += 1


        # # pop from the stack until you reach n-1 from the end, keep track of popped
        # if n == 1:
        #     stack.pop()
        #     if stack:
        #         node = stack.pop()
        #         node.next = None
        #     else: head = None

        # elif 1 < n < length:
        #     popped = 1
        #     while popped < n-1: 
        #         # n-1 will be the newSecond nodes
        #         # pop n
        #         # n-2.next will be newSecond node
        #         stack.pop()
        #         popped += 1
            
        #     secNode = stack.pop()
        #     stack.pop()
        #     firstNode = stack.pop()

        #     firstNode.next = secNode
        
        # elif n == length:
        #     popped = 1
        #     while popped < n-1:
        #         stack.pop()
        #         popped += 1
        #     node = stack.pop()
        #     head = node


        # return head

