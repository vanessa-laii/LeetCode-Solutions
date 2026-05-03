## Longest Consecutive Sequence 

### Intuition
- Turn into a set to remove duplicates
- if the value before does not exist, the start of a new seqence
- iterate until n+1 does not exist, that is your new length 
 

### Approach
**Data Structure:** 
set to remove duplicates and get O(1) accessing time


### Time Complexity
O(n) to iterate through the entire set


### Space Complexity
O(n) for the set