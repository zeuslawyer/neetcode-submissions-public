class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        last_seen = {}
        window_start = 0

        for i in range(len(s)):
            char = s[i]

            if char in last_seen and last_seen[char] >= window_start:
                window_start = last_seen[char] + 1

            last_seen[char] = i
            maxlen = max(maxlen, i - window_start + 1)

        return maxlen