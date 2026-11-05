class Solution:
    # Two pointers.  When we find a char, we move left to the char AFTER it.
    # Sets can be used for this. But for algoexpert variant we need a map
    # because sets do not get concatenated into string in the same order in which things were added.
    # see also https://www.algoexpert.io/questions/longest-substring-without-duplication
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <2: return len(s)

        indexOf = {}
        maxlen = 0
        longestStrIdxs = [0,0] # used only for algoexpert varient.

        left = 0
        for right in range(len(s)):
            char = s[right]
            
            if char in indexOf:
                # move left pointer
                left = max(indexOf[char] + 1, left)
            
            indexOf[char] = right
            maxlen = max(maxlen, right - left + 1)
            if right - left + 1 > longestStrIdxs[1] - longestStrIdxs[0] + 1:
                longestStrIdxs = [left, right]
            
        print(" The longest substring is:  ", s[longestStrIdxs[0] : longestStrIdxs [1] + 1])
        return maxlen




        

