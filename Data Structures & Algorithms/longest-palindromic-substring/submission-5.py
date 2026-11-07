class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Intuition - starting from each char, expand in both directions.
        # by starting at EACH char we capture substrings that are embedded in the middle of the string.
        # This makes each char a "centre" point to 
        # two types - even length and odd-len palindromes
        # handle both types.  Track the longest.

        longest = 0
        strStartIdx = 0

        for i in range(len(s)):
            # assume i is center of odd len palindrome. ==> single centre @ i.
            left, right = i, i

            # while its a palindrome....expand outwards both ways.
            while left >=0 and right < len(s) and s[left] == s[right]:
                strlen = right + 1 - left
                if strlen > longest:
                    strStartIdx = left
                    longest = strlen
                left -= 1
                right += 1
            

            # assume i is centre of even-len palindrome. Needs two centers.
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                strlen = right + 1 - left
                if strlen > longest:
                    strStartIdx = left
                    longest = strlen
                left -= 1
                right += 1
            

        return s[strStartIdx: strStartIdx + longest ]

                