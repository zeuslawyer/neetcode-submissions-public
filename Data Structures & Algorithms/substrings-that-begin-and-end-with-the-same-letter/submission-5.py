from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # WEIRD intuition. But if we maintain a count
        # that incremenents by the count of EACH letter
        # we get the answer

        # INTUITION: for any char ask "how many substrings end  start and end with the same letter (including this one single instance)?

        counts = defaultdict(int)
        total = 0

        for char in s:
            total += counts[char] + 1
            counts[char] += 1
        
        return total

