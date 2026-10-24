class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)

        numset = set(nums)
        longest = 0

        for num in nums:
           # find start of sequence. then keep increasing
           if num -1 not in numset:
                # sequence starts
                curr = num
                length = 0
                while curr in numset:
                    length +=1
                    curr = curr + 1
            
                longest = max(longest, length)
            
        
        return longest