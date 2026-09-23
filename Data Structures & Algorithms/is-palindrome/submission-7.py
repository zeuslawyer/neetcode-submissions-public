class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        s = s.replace(" ", "").lower()
        alphanums = ""
        for char in s:
            if char.isalnum(): alphanums+=char
        
        l, r = 0, len(alphanums)-1
        while l<r:
            if alphanums[l] != alphanums[r]: return False
            l+=1
            r-= 1
        
        return True
