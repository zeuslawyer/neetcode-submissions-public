from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_store = defaultdict(int)
        t_store = defaultdict(int)

        for i in range(len(s)):
            s_store[ord(s[i].lower()) - ord('a')] += 1
            t_store[ord(t[i].lower()) - ord('a')] += 1
        

        return s_store == t_store
        
    