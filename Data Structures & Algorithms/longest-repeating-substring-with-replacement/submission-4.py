class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # KEY intuition is that window must optimize for singe char repeating
        # which means in a given window (substring len) we must make Minimal edits 
        # => min edits + char with max freq = window size
        # => min edits = windowsize - char with max freq
        # so as long as min edits > k, keep shringing the window size

        l = 0
        longest = 0
        counts = {} # track freq of each letter

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r] ,0)
            
            # mostFrequent = max(counts.values())
            # numEditsNeeded = (r-l+1) - mostFrequent

            # while numEditsNeeded > k:
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
                # numEditsNeeded = (r-l+1) - max(counts.values())

            longest = max(longest, r-l+1) 

        return longest



