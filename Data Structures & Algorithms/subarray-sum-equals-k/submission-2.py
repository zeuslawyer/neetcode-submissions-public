class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalcounts = {0: 1}      # total: num times seen
        runningtotal = 0
        result = 0

        for i in range(len(nums)):
            runningtotal = runningtotal + nums[i]

            # negative complement - i.e. current running total - ? = k
            negativeComplement = runningtotal - k

            if negativeComplement in totalcounts:
                result += totalcounts[negativeComplement]

            if runningtotal in totalcounts:
                totalcounts[runningtotal] += 1
            else:
                totalcounts[runningtotal] = 1

        return result