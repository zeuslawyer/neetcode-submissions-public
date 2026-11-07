class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            # basecase - we have hit k constraint. Store copy of result so comb can be used in recursion
            if len(comb) == k:
                res.append(comb.copy())
                return

            # range is 1 to n, inclusive
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)

                # after we return from basecase, we pop current value to free up comb
                comb.pop()
    

        # range is 1 to n, inclusive
        backtrack(1, [])

        return res
