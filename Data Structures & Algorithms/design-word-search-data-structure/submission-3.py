class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordend = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.wordend = True
        

    def search(self, word: str, curr: Optional[TrieNode] = None) -> bool:
        if curr is None:
            curr = self.root
        for i in range(len(word)):
            char = word[i]
            if char == ".":
                # iterate over the tree nodes, and each of them will be the new root
                for node in curr.children.values():
                    found = self.search(word[i+1:], node)
                    if found: return True
                
                # after all iterations:
                return False
                        
            else: 
                if char not in curr.children:
                    return False
                
                curr = curr.children[char]
        
        return curr.wordend
