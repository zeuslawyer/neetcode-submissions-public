class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}


        def recurse(i, maxSoFar) -> int:
            if i >= len(nums): return 0

            if (i, maxSoFar) in cache: return cache[(i, maxSoFar)]

            # 2 paths possible. Based on whether the curr num < prevMax or not            
            # path 1 num is smaller which means we just skip this
            p1 = 0+recurse(i+1, maxSoFar)

            # path 2 num is > = which means we have found a subsequence start at at least 
            p2 = 0
            if maxSoFar < nums[i]:
                p2 = 1 +  recurse(i+1, nums[i])
            
            cache[(i, maxSoFar)] =  max(p1, p2)
            return cache[(i, maxSoFar)]

        return recurse(0, -math.inf)

