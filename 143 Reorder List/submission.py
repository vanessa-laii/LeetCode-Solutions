# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # The Question is asking for you to modify the list by starting from the outside l-r and moving inwards

        # Traverse the list and add all the nodes to the stack
            # The last node will be at the top of the stack
        
        stack = []
        temp = head
        lengthOfList = 0

        while temp:
            stack.append(temp)
            temp = temp.next
            lengthOfList += 1
        
        curr = head
        # Build the new linked list with the head and nodes in stack
        for iteration in range(lengthOfList//2):
            if stack:
                newNode = stack.pop()
            # store the node that curr is pointing too, before modifying
            futureNode = curr.next
            curr.next = newNode
            newNode.next = futureNode
            curr = futureNode
        
        # so you dont have a cycle!
        curr.next = None

            


        
        