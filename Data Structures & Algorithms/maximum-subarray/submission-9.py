class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        sumSoFar = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            sumSoFar += nums[i]
            maxSum = max(maxSum, sumSoFar)

            # Kadane's intuition: if the running sum is negative, adding it to future subarrays
            # will only reduce the sum of future subarrays, including single-digit subarrays
            if sumSoFar < 0:
                sumSoFar = 0
            
            

        return maxSum


