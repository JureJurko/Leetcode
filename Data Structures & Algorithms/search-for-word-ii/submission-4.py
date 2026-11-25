class TrieNode:
    def __init__(self, word_char=""):
        self.children = {}
        self.word = False
        self.word_char = word_char

class Dictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, words): # O(n)
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
            curr.word_char = word
    
    def search(self, word): # O(n)
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        visited = set()
        d = Dictionary()

        d.insert(words)
        results = set()


        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited:
                return

            element = board[r][c]
            if element in node.children:
                node = node.children[element]
            else:
                return

            if node.word:
                results.add(node.word_char)
            visited.add((r, c))

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            visited.remove((r, c))
        
        for i in range(ROW):
            for j in range(COL):
                dfs(i, j, d.root)
        
        return list(results)
