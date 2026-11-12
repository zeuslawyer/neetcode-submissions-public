class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        indexOf = {}
        maxlen = 0
        strIndexes = [0,0]

        l = 0
        for r in range(len(s)):
            char = s[r]

            if char in indexOf:
                # move left pointer to after that
                l = max(indexOf[char] + 1, l)

            # store current index against the char
            indexOf[char] = r

            # capture length of substr 
            maxlen = max(maxlen, r + 1 -l)

            if maxlen > strIndexes[1] - strIndexes[0]:
                strIndexes=[r,l]
            
        return maxlen





            


        