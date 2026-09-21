from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter, t_counter = {}, {}

        for i in range(len(s)):
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
            t_counter[t[i]] = 1 + t_counter.get(t[i], 0)
        return s_counter == t_counter
        
        
        # s_store = defaultdict(int)
        # t_store = defaultdict(int)

        # for i in range(len(s)):
        #     s_store[ord(s[i].lower()) - ord('a')] += 1
        #     t_store[ord(t[i].lower()) - ord('a')] += 1
        

        # return s_store == t_store

    