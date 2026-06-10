class PrefixTree:
    def __init__(self):
        self.children = {}
    
    @staticmethod
    def initialize_trie_with_board(board, max_len):
        x_board = len(board) - 1
        y_board = len(board[0]) - 1
        
        visited = set()

        def dfs(curr_x, curr_y, curr, depth):
            if curr_x > x_board or curr_y > y_board or depth > max_len:
                return
            
            curr_element = board[curr_x][curr_y]
            if curr_element not in curr.children:
                curr.children[curr_element] = PrefixTree()
            curr = curr.children[curr_element]

            visited.add((curr_x, curr_y))

            if curr_x > 0 and (curr_x - 1, curr_y) not in visited:
                dfs(curr_x - 1, curr_y, curr, depth + 1)
            if curr_x < x_board and (curr_x + 1, curr_y) not in visited:
                dfs(curr_x + 1, curr_y, curr, depth + 1)
            if curr_y > 0 and (curr_x, curr_y - 1) not in visited:
                dfs(curr_x, curr_y - 1, curr, depth + 1)
            if curr_y < y_board and (curr_x, curr_y + 1) not in visited:
                dfs(curr_x, curr_y + 1, curr, depth + 1)
                
            visited.remove((curr_x, curr_y))
        
        root = PrefixTree()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, 1)
        return root
    
    def search(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        max_len = max(len(w) for w in words) if words else 0
        
        prefix_tree = PrefixTree.initialize_trie_with_board(board, max_len)

        result = []
        for word in words:
            if prefix_tree.search(word):
                result.append(word)
        
        return result