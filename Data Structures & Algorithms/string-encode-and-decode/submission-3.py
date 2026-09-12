class Solution:
    DELIMITER ="#"

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + self.DELIMITER + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):

            # find DELIMITER and WORD LENGTH
            j = i
            while s[j] != self.DELIMITER:
                j+=1
            
            word_length = int(s[i:j]) # slice i:j instead of j-1 because encoded length may be > 1 digit
            word_index_start = j+1
            word_index_end = j+1 + word_length
            
            # next_word = s[j+1 : j+1 + word_length]
            # word = "".join(next_word)

            word = self.assemble_word(s, word_index_start, word_index_end)
            res.append(word)

            # update i
            i = j+1+word_length

        return res




    def assemble_word(self, s: str, start: int, end: int) -> str:
        word = s[start : end]
        return "".join(word)

