"""
Use intuition from combinations I and combinations sum II
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

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

        def recurse(idx, comboStr):
            # base case
            if len(comboStr) == len(digits) :
                res.append(comboStr)
                return
            
            # update state
            for char in digitToChar[digits[idx]]:
                updatedStr = comboStr+char
                recurse(idx + 1, updatedStr)

            # backtracking not needed because no compoud data structure


        recurse(0, "")
        return res