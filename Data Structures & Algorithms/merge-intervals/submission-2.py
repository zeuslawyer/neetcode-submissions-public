class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()

        output.append(intervals[0])

        for start,end in intervals[1:]:
            mergedIntervalstart = output[-1][0]
            mergedIntervalEnd = output[-1][1]
            
            if start <= mergedIntervalEnd:
                newIntervalEnd = max(mergedIntervalEnd, end)
                output[-1][1] = newIntervalEnd
            else:
                output.append([start, end])

        return output