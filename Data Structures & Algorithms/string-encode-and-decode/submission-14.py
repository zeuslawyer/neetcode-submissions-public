class Solution:

    def encode(self, strs: List[str]) -> str:
        DELIMITER = "#"
        encoded = ""

        for s in strs:
            # format is #5zubin#2is#5tired
            encoded += str(len(s)) +  DELIMITER + s
        return encoded

    def decode(self, s: str) -> List[str]:
        DELIMITER = "#"
        
        decoded =  []
        i = 0
        while i < len(s):
            j = i
            while s[j] != DELIMITER:
                j+=1
            
            strlen = int((s[i:j]))

            wordStartIndex = j+1 # char after the `#` delimiter

            word = s[wordStartIndex: wordStartIndex + strlen]
            decoded.append(word)

            i = j+1 + strlen
              
        
        return decoded



