class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        finalIntervals = []
        
        intervals = sorted(intervals)

        i = 1
        curr_min, curr_max = intervals[0]
        while i < len(intervals):
            if intervals[i][0] <= curr_max:
                curr_max = max(curr_max, intervals[i][1])
            else:
                finalIntervals.append([curr_min, curr_max])
                curr_min, curr_max = intervals[i]
            i += 1
        
        finalIntervals.append([curr_min, curr_max])

        return finalIntervals