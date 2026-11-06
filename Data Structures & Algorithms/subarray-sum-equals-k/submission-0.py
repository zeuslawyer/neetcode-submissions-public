class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalcounts = {0: 1}      # total: num times seend
        runningtotal = 0
        count = 0

        for i in range(len(nums)):
            runningtotal = runningtotal + nums[i]
            needed = runningtotal - k

            if needed in totalcounts:
                count = count + totalcounts[needed]

            if runningtotal in totalcounts:
                totalcounts[runningtotal] += 1
            else:
                totalcounts[runningtotal] = 1

        return count