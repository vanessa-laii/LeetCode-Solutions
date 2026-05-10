"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use a dictionary to store index: node
        # go through and make a copy of each node, then add to the dictionary

        if head is None:
            return None

        nodes = {}
        curr = head
        while curr:
            x, nxt, random = curr.val, None, None
            nodes[curr] = Node(x, nxt, random)
            curr = curr.next
        
        # go through again and grab the random and also reassign next
        """
        X (original node) -> x (copy node)
        """
        curr = head
        while curr:
            copy = nodes[curr]
            if curr.next:
                copy.next = nodes[curr.next]
            if curr.random:
                copy.random = nodes[curr.random]
            curr = curr.next
        
        return nodes[head]
            


        




        
        