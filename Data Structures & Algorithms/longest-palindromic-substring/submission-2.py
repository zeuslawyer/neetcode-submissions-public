class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        idx = 0
        longestLen = 0

        for i in range(len(s)):

            # substring is odd length
            left, right = i,i
            while left >=0 and right < len(s) and s[left] == s[right]:
                strLen = right-left+1

                # capture the longest string details
                if strLen > longestLen:
                    longestLen = strLen
                    idx = left
                left -= 1
                right += 1
            
            # substring is even length
            left, right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                strLen = right-left+1

                # capture the longest string details
                if strLen > longestLen:
                    longestLen = strLen
                    idx = left
                left -= 1
                right += 1
        
        return s[idx: idx + longestLen]

                


