from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxlen = 0

        for num in numset:
            if num - 1 not in numset:
                curr = num
                length = 0
                while (curr) in numset:
                    length+=1 
                    curr = curr = curr + 1
                
                maxlen = max(maxlen, length)
        
        return maxlen
