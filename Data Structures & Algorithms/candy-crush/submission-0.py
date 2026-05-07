class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board) # num of rows
        n = len(board[0]) # num of cols

        def find():
            crushed = set()
            for r in range(m):
                for c in range(n):
                    val = board[r][c]
                    if val == 0: # already crushed
                        continue
                    if c + 2 < n: # check 3 vertically
                        if board[r][c + 1] == val and board[r][c + 2] == val:
                            # update set with all 3
                            crushed.update([(r, c), (r, c + 1), (r, c + 2)])

                    if r + 2 < m: # check 3 horizontally
                        if board[r + 1][c] == val and board[r + 2][c] == val:
                            # update set with all 3
                            crushed.update([(r, c), (r + 1, c), (r + 2, c)])
            return crushed

        def crush(crushed):
            for r, c in crushed:
                board[r][c] = 0


        def drop():
            for c in range(n):
                write = m - 1 # start at bottom of board
                # scan col from bot to top
                for read in range(m - 1, -1, -1):
                    if board[read][c] != 0: # not crushed
                        board[write][c] = board[read][c]
                        write -= 1
                # clear all stale values to be 0
                while write >= 0: # handles "nothing to cleanup" case
                    board[write][c] = 0
                    write -= 1


        while True:
            crushed = find()
            if not crushed:
                break
            crush(crushed)
            drop()
        return board