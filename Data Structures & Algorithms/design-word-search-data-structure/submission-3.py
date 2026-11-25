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
        def dfs(word, curr, i):
            if i == len(word):
                return curr.word

            char = word[i]
            if char != ".":
                if char in curr.children:
                    return dfs(word, curr.children[char], i + 1)
                else:
                    return False
            else:
                return any(dfs(word, new_curr, i + 1) for new_curr in curr.children.values())
        
        return dfs(word, self.root, 0)
            
            
