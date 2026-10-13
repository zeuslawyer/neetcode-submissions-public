class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefixes, rightPrefixes = [0]* len(nums), [0] * len(nums)

        # left prefixes
        for i in range(len(nums)):
            if i == 0:
                leftPrefixes[i] = 1
            else:
                leftPrefixes[i] = leftPrefixes[i-1] * nums[i-1]
        
        # righ prefixes
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                rightPrefixes[i] = 1
            else:
                rightPrefixes[i] = rightPrefixes[i+1] * nums[i+1]
        

        res = []
        for i in range(len(nums)):
            res.append(leftPrefixes[i] * rightPrefixes[i])


        return res
        
