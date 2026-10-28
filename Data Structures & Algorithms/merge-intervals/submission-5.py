class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        # sorting on start time means that overlapping intervals are next to each other
        intervals.sort() 

        output.append(intervals[0])

        for newStart,newEnd in intervals[1:]:
            existingStart = output[-1][0]
            existingEnd = output[-1][1]

            if newStart <= existingEnd:
                newIntervalEnd = max(existingEnd, newEnd)
                
                # update only the most recently merged interval
                output[-1][1] = newIntervalEnd
            else:
                # since there is no overlap push the new interval
                output.append([newStart, newEnd])

        return output