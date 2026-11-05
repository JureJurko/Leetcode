from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        COL, ROW = len(board), len(board[0])

        for c in range(COL):
            for r in range(ROW):
                col_box = c // 3
                row_box = r // 3
                k = (col_box, row_box)
                el = board[c][r]
                if el == ".":
                    continue
                elif el in rows[r] or el in cols[c] or el in boxes[k]:
                    return False

                rows[r].add(el)
                cols[c].add(el)
                boxes[k].add(el)
        
        return True

                