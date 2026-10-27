from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # store s1 in table
        s1KeyTup = self.getKeyTup(s1)


        windowlen = len(s1)
        # include last char
        for i in range(len(s2)-windowlen + 1):
            # slice from i onwards
            substr = s2[i: i + windowlen]
            keyTup = self.getKeyTup(substr)
            if keyTup == s1KeyTup:
                return True

        return False


    def getKeyTup(self, s:str)->list[int]:
        key =[0] * 26
        for char in s:
            idx = ord(char)-ord('a')
            key[idx] += 1
        return tuple(key)



        

        
        