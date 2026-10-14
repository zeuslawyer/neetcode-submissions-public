class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        sumSoFar = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            if sumSoFar < 0:
                sumSoFar = 0
            
            sumSoFar += nums[i]
            maxSum = max(maxSum, sumSoFar)
            
            

        return maxSum


