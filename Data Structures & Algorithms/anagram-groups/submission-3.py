class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # SORTING : O(M * NlogN)
        group = {}

        for s in strs:
            # sortedstr = tuple(sorted(s))
            # or 
            sortedstr = "".join(sorted(s))
            bucket = group.get(sortedstr, [])
            bucket.append(s)
            group[sortedstr] = bucket

        return list(group.values())
        