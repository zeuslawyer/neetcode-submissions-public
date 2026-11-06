class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        sumSoFar = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            sumSoFar += nums[i]
            maxSum = max(maxSum, sumSoFar)

            # Kadane's intuition: if the running sum becomes negative, keeping it will only reduce the sum of any future subarray, because a subarray can be a single digit too
            if sumSoFar < 0:
                sumSoFar = 0
            
            

        return maxSum


