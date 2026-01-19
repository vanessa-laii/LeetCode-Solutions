## 143. Reorder List

### Intuition
Question wants to modify the order of the linked list alternating between the left most and right most elements. With linked lists, we need to traverse through the entire list to access and modify the right most elements.  

### Approach
**Data Structure:** 
- Stack: LIFO structure is good for storing the nodes of the linked list and accessing from the top

Append all the elements of the LL into the stack and also keep track of the length of the list for building the loop later on. 
- Assign the current node.next to a variable 
- The node popped from the stack is the new node that the current will point to. 

The order goes:
current node -> popped node -> original current.next node (var futureNode) 

- move the pointer of current to the last node we added, the original current.next node

Lastly, so you don't have a cycle, we need to end the LL by assigning current.next as None. This will cut off any remaining links.


### Time Complexity
O(n) for the stack, O(n) for the loop

Thus, O(n)


### Space Complexity
O(N) memory for the stack