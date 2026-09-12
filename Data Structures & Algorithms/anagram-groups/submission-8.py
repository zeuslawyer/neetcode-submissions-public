class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # tuple as key
        grouped = {}

        for s in strs:
            counter = [0] * 26
            for char in s:
                letter_index = ord(char)-ord('a')
                counter[letter_index]+=1
            
            key = tuple(counter)
            val = grouped.get(key, [])
            val.append(s)
            grouped[key] = val
        
        return list(grouped.values())



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
        