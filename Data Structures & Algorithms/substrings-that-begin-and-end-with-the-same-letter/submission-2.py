class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # WEIRD intuition. But if we maintain a count
        # that incremenents by the count of EACH letter
        # we get the answer

        # INTUITION: for any char ask "how many substrings end  start and end with the same letter (including this one single instance)?

        lettercounts = [0]* 26 # store array of alphabet indexed by alphabet

        ansCount = 0

        for char in s:
            idx = ord(char) - ord('a')
            lettercounts[idx]+=1
            ansCount += lettercounts[idx]
        
        return ansCount

