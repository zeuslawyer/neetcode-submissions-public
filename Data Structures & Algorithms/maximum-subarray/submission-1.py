class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        maxSum= nums[0]
        sum = 0

        for i in range(len(nums)):
            # resetting sum effectively starts new sub array compputation
            if sum < 0:
                sum = 0
            
            sum += nums[i]
            maxSum = max( sum, maxSum)
            

        return maxSum
        