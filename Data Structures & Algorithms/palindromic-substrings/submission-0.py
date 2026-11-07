class Solution:
    def countSubstrings(self, s: str) -> int:
        # Same intuition as finding longest palindromic substr.  
        # check if each char is the centre of even AND odd len palindrome
        # if it is palindrome, capture state and expand outwards.

        count = 0
        for i in range(len(s)):
            # if odd len
            left = right = i
            
            #while its a palindrome expand both ways
            while left >=0 and right < len(s) and s[left]==s[right]:
                count += 1
                left -= 1
                right += 1




            # if even len
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left]==s[right]:
                count += 1
                left -= 1
                right += 1
            

        return count