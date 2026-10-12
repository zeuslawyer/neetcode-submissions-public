class Solution:
    # Two Pointers with DP 
    def longestPalindrome(self, s: str) -> str:
        residx = 0
        reslen = 0

        for i in range(len(s)):
            # center, if odd len
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                strlen = right-left + 1

                # update DP store of len if this strlen is now longer than longest so far
                if strlen > reslen:
                    reslen = strlen
                    residx = left
                
                # expand outwards from center
                left -=1
                right +=1
            

            # center if even len
            left, right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                strlen = right-left+1

                if strlen > reslen:
                    reslen = strlen
                    residx = left
                
                left-=1
                right+=1
            
        return s[residx:residx + reslen]
                

