class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children =  {}
        self.is_word: bool = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        
        for char in word:
            if not char in current.children:
                current.children[char] = TrieNode(val=char)
            current = current.children[char]
        current.is_word = True

   
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return True
        
        