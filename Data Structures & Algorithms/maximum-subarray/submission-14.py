class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        runningTotal = 0
        maxSum = -math.inf # or nums[0]

        for num in nums:
            runningTotal += num
            maxSum = max(runningTotal, maxSum)

        # if the running sum becomes negative, keeping it will only 
        # reduce the sum of any future subarray.
        # so reset it
            if runningTotal < 0:
                runningTotal = 0
        

        return maxSum
