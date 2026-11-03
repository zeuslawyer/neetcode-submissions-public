class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we track counts of each char needed, and what we have, at char level 
        #  We also track  total counts of whats needed vs what we have
        # when the totals are equal we start to increase LEFT pointer to shorten window
        # and adjust counts accordingly.

        windowCounts, inputCounts = {}, {}

        for char in t:
            windowCounts[char] = 0
            inputCounts[char] = inputCounts.get(char, 0) + 1
        
        # need counts the total num of UNIQUE characters in t
        uniqueCharsNeeded = len(inputCounts)

        # completeCharSetsInWindow only updates if a chars count in the window = the char's count in inputCounts
        completeCharSetsInWindow = 0 

        left = 0
        windowIndexes = []
        windowLen = math.inf

        for right in range(len(s)):
            char = s[right]
            # update the counts
            windowCounts[char] = 1 + windowCounts.get(char, 0)
            
            # if we have the required num of that char
            if char in inputCounts and windowCounts[char] == inputCounts[char]:
                completeCharSetsInWindow +=1
            
            # If haves == needs, then time to start shrinking the window
            while completeCharSetsInWindow == uniqueCharsNeeded:
                # check the len of the string at each stage. If shorter, 
                # updated windowLen and the pointers
                if (right - left + 1) < windowLen:
                    windowLen = right - left  + 1
                    windowIndexes = [left, right]
                
                # pop left char
                leftChar = s[left]
                windowCounts[leftChar] -= 1
                if leftChar in inputCounts and windowCounts[leftChar] < inputCounts[leftChar]:
                    completeCharSetsInWindow -= 1
                
                left += 1
        
        if windowLen != math.inf:
            l, r = windowIndexes
            return s[l : r+1]
        else:
            return ""
                


