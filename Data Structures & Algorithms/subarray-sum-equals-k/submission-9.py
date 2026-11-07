class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCounts = {0 : 1} # => prefixSum of 0 is seen once, imaginary before nums[0]

        res = 0
        currTotal = 0 # tracking the current incremental sum in the array
        for num in nums:
            currTotal += num

            # the negative complement prefix sum X such that currTotal - X = k
            # result the total COUNTS of all values X,  added up
            prefixSumComplement = currTotal -  k

            # if it is present in map, then that is the number of subarrays possible that
            # which chopped off (i.e deducted) from currTotal will = k

            if prefixSumComplement in prefixSumCounts:
                res += prefixSumCounts[prefixSumComplement]
            
            # add the current running total as a "seen" prefixSum 
            prefixSumCounts[currTotal] = prefixSumCounts.get(currTotal,  0) + 1
        
        return res
            


