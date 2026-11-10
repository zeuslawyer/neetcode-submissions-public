class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0

        cache = {} # keys are tuples of (i.j)


        def recurse(i, j):
            # base case out of bounds. If so then no subsequence possible.
            if i >= len(text1) or j >= len(text2):
                return 0

            
            # memoize / Update state
            if (i,j) in cache:
                return cache[(i,j)]
            
            # if chars are equal then its a subsequence. Increment and move both pointers
            if text1[i] == text2[j]:
                cache[(i,j)] = 1 + recurse(i+1, j+1)
            else:
                # longest requures max of the two branches
                cache[(i,j)] = max(recurse(i+1, j) , recurse(i, j+1))

            return cache[(i,j)]
            
        return recurse(0,0)


        

        