class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            sortedstr = tuple(sorted(s))
            bucket = group.get(sortedstr, [])
            bucket.append(s)
            group[sortedstr] = bucket

        return list(group.values())
        