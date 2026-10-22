class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        arrlen = len(nums)+1

        for right in range(len(nums)):
            sum+= nums[right]

            while sum >= target:
                window = right-left +1
                arrlen = min(arrlen, window)
                sum -= nums[left]
                left += 1
        
        return arrlen if arrlen != len(nums) + 1 else 0


        