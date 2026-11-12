class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}

        def recurse(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if ((i, j)) in cache:
                return cache[(i, j)]

            # if the chars match then we have a subsequence. chop off
            # those chars by incrementing idxs
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + recurse(i + 1, j + 1)

            else:
                cache[(i, j)] = max(recurse(i + 1, j), recurse(i, j + 1))

            return cache[(i, j)]

        return recurse(0, 0)
