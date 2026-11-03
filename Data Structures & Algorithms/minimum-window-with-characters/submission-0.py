class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we track counts of each char needed, and what we have, at char level 
        #  We also track  total counts of whats needed vs what we have
        # when the totals are equal we start to increase LEFT pointer to shorten window
        # and adjust counts accordingly.

        windowCounts, inputCounts = {}, {}

        # need counts the total num of UNIQUE characters in t
        need, have = 0 , 0

        for char in t:
            windowCounts[char] = 0
            inputCounts[char] = inputCounts.get(char, 0) + 1
        
        need = len(inputCounts)

        left = 0
        windowIndexes = []
        windowLen = math.inf

        for right in range(len(s)):
            char = s[right]
            # update the counts
            windowCounts[char] = 1 + windowCounts.get(char, 0)
            
            # if we have the required num of that char
            if char in inputCounts and windowCounts[char] == inputCounts[char]:
                have +=1
            
            # If haves == needs, then time to start shrinking the window
            while have == need:
                # check the len of the string at each stage. If shorter, 
                # updated windowLen and the pointers
                if (right - left + 1) < windowLen:
                    windowLen = right - left  + 1
                    windowIndexes = [left, right]
                
                # pop left char
                leftChar = s[left]
                windowCounts[leftChar] -= 1
                if leftChar in inputCounts and windowCounts[leftChar] < inputCounts[leftChar]:
                    have -= 1
                
                left += 1
        
        if windowLen != math.inf:
            l, r = windowIndexes
            return s[l : r+1]
        else:
            return ""
                


