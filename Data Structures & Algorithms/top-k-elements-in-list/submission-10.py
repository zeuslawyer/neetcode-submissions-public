class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if not num in hash:
                hash[num] = 1
            else:
                hash[num] += 1


        pairs = []
        for num, count in hash.items():
            pairs.append([num, count])

        def sorter(pair):
            return pair[1]
        
        pairs.sort(key=sorter)

        res = []
        for i in range(k):
            res.append(pairs.pop()[0])

        return res
