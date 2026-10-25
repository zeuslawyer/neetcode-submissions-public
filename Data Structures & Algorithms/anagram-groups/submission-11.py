from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sortedstring = "".join(sorted(s))
            hashmap[sortedstring].append(s)
        
        return list(hashmap.values())