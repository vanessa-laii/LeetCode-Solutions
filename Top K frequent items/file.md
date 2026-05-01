## Top K frequent elements

### Intuition
- build a counter for the frequency
- build a min heap for the values - poping from a min heap removes the smallest values
- store tuples in the heap
- [num for value, num in heap] returns a list of all the vlaues in the heap
 

### Approach
**Data Structure:** 
min heap since we want to sort the values 


### Time Complexity
O(n) to iterate through the heap of all the nodes


### Space Complexity
O(n) for the heap and counter