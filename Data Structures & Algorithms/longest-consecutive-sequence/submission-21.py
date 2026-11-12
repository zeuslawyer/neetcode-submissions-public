class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlength = 0

        for num in nums:
            if not (num - 1) in numset:
                # start of a new sequence. 
                # numset.add(num)
                length = 0

                #  Num already in set. 
                curr = num
                while curr in numset:
                    length += 1
                    curr = curr+1
                
                maxlength = max(maxlength, length)
        
        return maxlength

                



        