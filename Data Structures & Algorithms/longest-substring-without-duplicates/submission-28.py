# using just set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        seen = set()
        maxlen = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            
            while char in seen:
                # remove all characters left is pointing to until the repeated char is also removed.
                seen.remove(s[left])
                left +=1 
            
            seen.add(char)
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen


        