class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Intuition: Sort. then  track the prevEnd for each iteration.  It updates based on which interval we choose to "keep" -- we keep the one with the smallest end time
        We need to remove min number of OVERLAPPING intervals
        """

        intervals.sort()

        prevend = intervals[0][1]
        removed = 0
        for i in range(1, len(intervals)):
            currstart, currend = intervals[i]

            # if NOT overlapping, move on after updating preevend
            if currstart >= prevend:
                prevend = currend

            # overlapping
            else:
                # of the two overlapping segments we keep the one with the smaller end time
                # and we "remove" the other so increment.
                prevend = min(currend, prevend)
                removed += 1
        
        return removed
            









