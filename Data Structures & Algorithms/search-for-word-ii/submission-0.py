# INTUITION - same as find words I.  Use DFS + Backtracking. But we use a trie to store all words and then while DFSing we try and trace prefixes that exist in Trie.

class Trie:
    def __init__(self):
        self.children = {} # char <> Trie node
        self.isWord = False
    
    def addWord(self, w):
        curr = self

        for c in w:
            if not c in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixtree = Trie()

        for word in words:
            prefixtree.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        found = set()
        visited =set()

        def dfs(r, c, trienode, strSoFar ):
            # all base cases
            if (r,c) in visited: return
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS): return
        
            if board[r][c] not in trienode.children: return # its not one of the words

            # update state
            visited.add((r,c))
            trienode = trienode.children[board[r][c]]
            strSoFar += board[r][c]
            
            if trienode.isWord:
                found.add(strSoFar)

            dfs(r+1, c, trienode, strSoFar )
            dfs(r-1, c, trienode, strSoFar )
            dfs(r, c + 1, trienode, strSoFar )
            dfs(r, c-1, trienode, strSoFar )

            # Backtrack
            visited.remove((r,c))



        for r in range(ROWS):
            for c in range(COLS):
                strSoFar = ""
                dfs(r, c, prefixtree, strSoFar)
        
        return list(found)


