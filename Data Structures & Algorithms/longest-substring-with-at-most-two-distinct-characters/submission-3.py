class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charcounts = {} # repeat chars are alloed so we hold counts

        longest = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            charcounts[char] = 1 + charcounts.get(char, 0)
            
            while len(charcounts) > 2:
                # shrink window from the left ptr.
                # shrinking means removing that char from the count.
                # if char is done, del it.
                charcounts[s[left]] -=1
                if charcounts[s[left]] == 0:
                    del charcounts[s[left]]
                
                left +=1

            longest = max(longest, right-left + 1)
      
        return longest



        