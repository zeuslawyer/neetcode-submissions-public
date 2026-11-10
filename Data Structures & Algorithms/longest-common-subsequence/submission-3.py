class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Intuition: if the curr chars match, then += 1. 'Chop' that letter off and you're left with the SAME subproblem for the rest of the two strings.

        if chars !== then we branch 2 ways. pointer on one str increases and the other doesnt.  this happens for both strings. now we have the same subproblem, but with different strings.  

        and so on it recurses until we hit the end of the shorter string. Then no more subsequences are possible so we return.   BASE CONDITION.
        """


        # memoize
        cache = {} # use tuples of (i,j) as keys


        # we write a helper rather than reuse function so that we dont need to 
        # slice the strings and add to memory complexity.
        # i and j are pointers to str1 and str 2

        def recurse(i, j):
            # base condition
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]

            # Update states for both remaining possibilities.
            if text1[i] == text2[j]:
                # we need to increment the counter for subsequence.
                # and we increment BOTH pointers.
                cache[(i,j)]  =  1 + recurse(i+1, j+1)            
            else:
                cache[(i,j)] = max(recurse(i + 1, j), recurse(i, j+1))
            
            return cache[(i,j)]



        return recurse(0,0)
        


        