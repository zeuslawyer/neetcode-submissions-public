class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def recurse(idx, accum=""):
            # base conditions
            if len(accum) == len(digits):
                res.append(accum)
                return

            # updating state + backtracking
            d = digits[idx]

            for char in digitToChar[d]:
                updatedAccum = accum+char
                recurse( idx + 1, updatedAccum)

            # no backtracking needed as str is not passed by reference.

        
        recurse(0, "")

        return res
        