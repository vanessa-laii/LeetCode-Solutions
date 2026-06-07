class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for start, end in intervals:
            # new interval completely before, add new interval, save current interval as new interval
            if start > newInterval[1]:
                result.append(newInterval)
                newInterval = [start, end]

            # new interval completely after
            # just add the interval
            elif newInterval[0] > end:
                result.append([start, end])
            # overlapping
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        
        result.append(newInterval)
        return result
