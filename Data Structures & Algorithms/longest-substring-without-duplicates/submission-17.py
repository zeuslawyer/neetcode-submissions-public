class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        last_seen = {}
        window_start = 0

        for i in range(len(s)):
            char = s[i]
            
            # at this char, has it been seen and was it last seen inside 
            # the current window? 
            # current window is i - window_start
            # if yes, then start a new window after the one that was last seen.
            if char in last_seen and last_seen[char] >= window_start:
                window_start = last_seen[char] + 1

            # REGARDLESS of the above we need to update the last seen index of the curr char and capture the window lenght at EACH iteration
            last_seen[char] = i
            maxlen = max(maxlen, i - window_start + 1)

        return maxlen