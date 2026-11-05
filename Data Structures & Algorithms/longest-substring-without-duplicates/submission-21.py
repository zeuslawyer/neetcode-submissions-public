# instead of set using a hashtable so that we can ALSO return the string.
# sets arent ordered so converting to a string with "".join may produce wrong res.
# hashtable stores index of each char last seen.
# two pointers.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {} # char <> index

        left = 0
        maxlength = 0
        fullstr = "" # only added for algoexpert version

        for right in range(len(s)):
            char = s[right]

            if char in lastSeen:
                # update left index
                left = max(lastSeen[char] + 1, left)

            lastSeen[char] = right
            maxlength = max(maxlength, right - left + 1)


        print(fullstr)
        return maxlength
