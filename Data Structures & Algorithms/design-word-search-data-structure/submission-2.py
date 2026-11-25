class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(word, curr):
            if not word:
                return curr.word
            
            char = word[0]
            if char != ".":
                if char in curr.children:
                    return dfs(word[1:], curr.children[char])
                else:
                    return False
            else:
                return any(dfs(word[1:], new_curr) for new_curr in curr.children.values())
        
        return dfs(word, self.root)
            
            
