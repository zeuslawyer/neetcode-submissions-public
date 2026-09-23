from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for i in range(len(nums)):
            counts[nums[i]] += 1
        

        maxlen = 0

        for i in range(len(nums)):
            num = nums[i]
            if counts.get(num-1):
                # this num is not the start of a sequence
                continue 
            
            length = 1
            while (num + 1) in counts:
                length+=1
                num = num+1
            maxlen = max(maxlen, length)
                
        return maxlen   

            


