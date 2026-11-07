class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # highest summing / lowest summing, seen across ALL indices
        globalMaxSubarray, globalMinSubarray = nums[0], nums[0] 

        # highest summing / lowest summing, seen at THIS idx
        localMaxSubarray = localMinSubarray = 0

        runningTotal = 0

        for i, num in enumerate(nums):
            # track the running total. Because the total of the NON LOOPING array is used later.  
            runningTotal += num
            
            # include the local max sub array so far OR start afresh
            localMaxSubarray = max(num, localMaxSubarray + num)
            localMinSubarray = min(num, localMinSubarray + num)

            # update the global maximum if needed.
            globalMaxSubarray = max(globalMaxSubarray, localMaxSubarray)
            globalMinSubarray = min(globalMinSubarray, localMinSubarray)


        # INTUTION.  TOTAL of the entire array *minus* 
            #NON LOOPING global min subarray gives us GLOBAL max subarray, even if it loops.
        # if globalMaxSubarray is -ve then we we return that directly
        return globalMaxSubarray if globalMaxSubarray < 0 else max(globalMaxSubarray, runningTotal - globalMinSubarray)