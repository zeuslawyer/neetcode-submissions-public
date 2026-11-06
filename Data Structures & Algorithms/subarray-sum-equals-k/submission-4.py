class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalcounts = {0: 1}  # key is a givenprefixsum outcome. Val is count of frequency - how often seen so far. Initialized to the prefix sum out of bounds on LHS - its a sum of 0.  seen once. 

        runningtotal = 0
        result = 0

        for i in range(len(nums)):
            runningtotal = runningtotal + nums[i]

            # negative complement - i.e. current running total - ? = k
            negativeComplement = runningtotal - k

            # check first if negative complement has been counted before add that result because hey're the number of previous PREFIX subarrays that can be CHOPPED of the current subarray at (i) and the remaining subarray  sums to == k
            if negativeComplement in totalcounts:
                result += totalcounts[negativeComplement]

            # add the current running total as it is a future prefix sum to check
            if runningtotal in totalcounts:
                totalcounts[runningtotal] += 1
            else:
                totalcounts[runningtotal] = 1


        return result
