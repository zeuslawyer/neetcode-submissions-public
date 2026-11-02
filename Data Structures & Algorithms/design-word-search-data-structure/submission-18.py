class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.wordend = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(val=char)
            curr = curr.children[char]
        curr.wordend = True
        

    def search(self, word: str, node: Optional[TrieNode]=None) -> bool:
        curr = self.root if node is None else node

        for i in range(len(word)):
            char = word[i]

            if char != ".":
                if char not in curr.children:
                    return False # exit condition
                curr = curr.children[char]
            else:
                # Wildcard match
                for node in curr.children.values():
                    found = self.search(word[i+1: ], node)
                    if found:
                        return True # exit condition
                
                # at the end of the loop
                return False

        return curr.wordend