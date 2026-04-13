class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # verify no dupes in the following:
        # use sets to keep track of: rows, cols, boxes
        # boxes:  r // 3, c // 3 


        # core logic: loop through every single cell in the 9x9
        # if cewll is "." (empty) , skip / continue
        #   check if it's already in row[r] set, col[c] set, or box[r//3, c//3] set
            # if so, return false
        # end of loop, return true
        rows_set = collections.defaultdict(set)
        cols_set = collections.defaultdict(set)
        box_set = collections.defaultdict(set)

        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_set[r]) or (board[r][c] in cols_set[c]) or (board[r][c] in box_set[r//3, c//3]):
                    return False
                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                box_set[r//3, c//3].add(board[r][c])
        return True