"""
Intuition - same approach as Combination - I
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recurse(start, combos, total):
            # base cases
            if start >= len(nums) or total > target:
                return
            if total == target:
                res.append(combos.copy()) # copy so that combos can be used in recursion
                return
            
            for i in range(start, len(nums)):
                total += nums[i]
                combos.append(nums[i])
                recurse(i, combos, total) # since we can reuse i we dont need i+1 here.

                # backtrack and pop after returning from base condition
                combos.pop()
                total -= nums[i]

        recurse(0, [], 0)

        return res