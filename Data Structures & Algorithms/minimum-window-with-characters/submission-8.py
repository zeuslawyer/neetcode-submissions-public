class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we track counts of each char needed, and what we have, at char level 
        #  We also track  total counts of whats needed vs what we have
        # when the totals are equal we start to increase LEFT pointer to shorten window
        # and adjust counts accordingly.
        tcounts, windowcounts = {}, {}

        # initialize count values for each char in t.
        for char in t:
            tcounts[char] = 1 + tcounts.get(char, 0)
            windowcounts[char] = 0
        
        #  each char's set completes only when the windowCharsetsCount[char] 
        # = tcharsetCount[char]
        tcharsetCount = len(tcounts) # need
        windowCharsetsCount = 0 # have

        # right pointer expands until windowcount[char] is == tcharsetCount[char].
        # left pointer moves to shrink window when that happens.
        # we track the tcharsetCount and windowCharsetCount.

        left = 0
        windowLen = math.inf
        indexes =[left, len(t)-1]
        for right in range(len(s)):
            ch = s[right]
            windowcounts[ch] = 1 + windowcounts.get(ch ,0) 

            if ch in tcounts and windowcounts[ch] == tcounts[ch]:
                windowCharsetsCount+=1

            while windowCharsetsCount == tcharsetCount:
                # capture window size
                if (right - left + 1) < windowLen:
                    windowLen = right-left+1
                    indexes = [left, right]

                # window that contains `t` is found. Start shrinking window.
                leftchar = s[left]
                left += 1
                windowcounts[leftchar] -= 1
                if leftchar in tcounts and windowcounts[leftchar] < tcounts[leftchar]:
                    windowCharsetsCount -= 1
            

        if windowLen != math.inf:
            l,r = indexes
            return s[l: r+1]        
        else:
            return ""




