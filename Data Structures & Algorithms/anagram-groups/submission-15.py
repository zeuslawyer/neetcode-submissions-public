from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for s in strs:
            # construct a tuple of the alphabet and char count
            counts = [0] * 26
            for char in s:
                idx = ord(char.lower()) - ord('a')
                counts[idx] += 1

            countsTup = tuple(counts)
            groups[countsTup].append(s)

        return list(groups.values())



        