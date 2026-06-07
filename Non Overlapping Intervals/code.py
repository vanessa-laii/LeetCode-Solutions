class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        start, end = intervals[0]
        remove = 0
        # greedy solution, keep the one that ends first

        for i in range(1, len(intervals)):
            # if overlapping
            if intervals[i][0]  < end :
                remove += 1
                start, end = start, min(intervals[i][1], end)
            else:
                start, end = intervals[i]
        
        return remove