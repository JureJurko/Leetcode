class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None                  # the full word if one ends here


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        found = []

        def dfs(r, c, parent):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            ch = board[r][c]
            node = parent.children.get(ch)
            if not node:
                return

            if node.word:
                found.append(node.word)
                node.word = None

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, node)
            board[r][c] = ch

            if not node.children and not node.word:
                del parent.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return found