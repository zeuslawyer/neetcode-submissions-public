class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numset = set(nums)

        maxlen = 0
        for num in nums:
            if num-1 not in numset:
                # we have start of sequence
                length = 1 
                curr = num + 1
                while (curr in numset):
                    length+=1
                    curr = curr + 1
                
                maxlen = max(maxlen, length)
        
        return maxlen
