
# Sliding Window -- pruning left side until we meet the constraint
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = {}
        longest = 0
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            counts[char] = 1 + counts.get(char, 0)

            # shrink from left where it exceeds the constraint
            # shrink window - reduce the counts and move left ptr
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]] #remove if char is not in window anymore
                left +=1 
            

            longest = max(longest, right - left + 1)

        return longest

                
