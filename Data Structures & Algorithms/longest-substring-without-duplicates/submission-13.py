class Solution:
    # not ideal.... see next one
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        left = 0
        seen = set()
        longest = 0

        for right in range( len(s)):
            if not s[right] in seen:
                seen.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                # found a repeat, start to shrink the window
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])
        
        return longest
        





        