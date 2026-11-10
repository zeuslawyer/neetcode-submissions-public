# KADANES
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        runningTotal = 0
        maxSumSoFar =  nums[0] # or -math.inf 

        for num in nums:
            runningTotal += num
            maxSumSoFar = max(runningTotal, maxSumSoFar)

        # if the running sum becomes negative, keeping it will only 
        # reduce the sum of any future subarray.
        # so reset it
            if runningTotal < 0:
                runningTotal = 0
        

        return maxSumSoFar

 

"""
globalMaxSum = nums[0]
        maxSumSoFar = 0

        for num in nums:
            maxSumSoFar = max(num, num + maxSumSoFar)
            globalMaxSum = max(globalMaxSum, maxSumSoFar)
        
        return globalMaxSum
       
"""