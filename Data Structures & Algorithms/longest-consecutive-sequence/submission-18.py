class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0 
        for num in nums:
            # Start of sequence means num-1 is not in the set yet
            if num-1 not in numset:
                seqLength = 0
                curr = num
                while curr in numset:
                    seqLength += 1
                    curr = curr + 1 # consecutive sequence
                
                longest = max(longest, seqLength)
        
        return longest


                