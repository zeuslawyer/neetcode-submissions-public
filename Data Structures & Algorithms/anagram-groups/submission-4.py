class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # tuple as key
        # grouped

        # SORTING : O(M * NlogN)
        grouped = {}

        for s in strs:
            sortedstr = tuple(sorted(s))
            # or 
            # sortedstr = "".join(sorted(s))
            bucket = grouped.get(sortedstr, [])
            bucket.append(s)
            grouped[sortedstr] = bucket

        return list(grouped.values())
        