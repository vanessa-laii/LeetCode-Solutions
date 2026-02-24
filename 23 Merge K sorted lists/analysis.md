## 143. Reorder List

### Intuition
- build a min heap of all the head nodes since that is what is in lists
- create a dummy node and build the answer linked list by popping from the heap
- as you pop and update the pointers, push in the next node in each sub LL
 

### Approach
**Data Structure:** 
min heap since we want to sort the values of the nodes in increasing order


### Time Complexity
O(n) to iterate through the heap of all the nodes


### Space Complexity
O(n) for the heap