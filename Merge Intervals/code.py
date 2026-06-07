class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        # need to sort
        intervals.sort(key = lambda x:x[0])
        for interval in intervals:
            if stack:
                lastStart, lastEnd = stack[-1]
                if interval[0] <= lastEnd:
                    stack.pop()
                    stack.append((lastStart, max(lastEnd, interval[1])))
                else:
                    stack.append((interval[0], interval[1]))
            
            else:
                stack.append((interval[0], interval[1]))
        
        return stack
        