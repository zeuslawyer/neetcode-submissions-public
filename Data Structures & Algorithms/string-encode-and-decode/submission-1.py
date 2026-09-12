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
            
            word_length = int(s[i:j])
            next_word = s[j+1 : j+1 + word_length]

            word = "".join(next_word)
            res.append(word)

            # update i
            i = j+1+word_length
            
        return res




    def assemble_word(self, s : str,start: int, length:int) -> str:
        chars =[]
        for i in range(start, start+length):
            chars.append(s[i])
        
        return "".join(chars)



    #     loop over index of str 
    #     look for the DELIMITER
    #     read preceding char to get len of word
    #     mini subloop of len = len of word
    #     join into string
    #     push to res




