"""
Intuition: recursively build combinations.
since (1,2) is same as (2,1) at any position i in input, we only move forward
to i + 1.  We dont need to do  < i because that would include future combinations at
indices > i.

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] # holds resulting combos of size k

        def recurse(start, combo):
            # base case, combo has hit k len
            if len(combo) == k:
                res.append(combo.copy()) # copy only, so we can reuse combo
                return

            
            # end at n+1 because its inclusive of n
            for i in range(start, n+1):
                combo.append(i)
                recurse(i+1, combo)

                # we pop after we return from recursion to clear space in 
                # combo for reuse
                combo.pop()

        recurse(1, combo = [])

        return res

