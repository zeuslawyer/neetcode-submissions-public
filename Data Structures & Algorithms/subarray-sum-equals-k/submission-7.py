class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCounts = {0: 1} # single count of  sum 0 because it exists before nums starts as baseline

        result = 0
        currentSum = 0
        for num in nums:
            currentSum += num

            # find the negative complement X such that currentSum - X = k
            negComp = currentSum - k

            # if its in the dict, then it can be "chopped of" 
            # the current full length sub array up to and including num
            # and we'd STILL get k.
            # We do this BEFORE we update prefixSumCounts with the currentSum to handle situation where k =0 in which case prefixSumCounts of current sum and neg comp are == 
            if negComp in prefixSumCounts:
                result += prefixSumCounts[negComp]
            
            prefixSumCounts[currentSum] = 1 + prefixSumCounts.get(currentSum, 0)

        return result
