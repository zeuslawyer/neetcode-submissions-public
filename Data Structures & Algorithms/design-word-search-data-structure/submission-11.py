class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.wordend = False

# DFS
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        
        curr.wordend = True
        

    # recursive DFS
    def search(self, word: str, curr: Optional[TrieNode] = None) -> bool:
        if curr is None:
            curr = self.root
            # no other base condition because the function return True or False
        # if curr.wordend: return True

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
