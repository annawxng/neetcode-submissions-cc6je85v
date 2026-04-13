class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 3 conditions - sameCol, posDiag, negDiag
        # we dont track rows bc we place one queen prer row only

        # init stuff
        # backtrack: start from row 0 all the way to row n
            # base case: row == n, we save our result and return
            # loop through each col
                # if passes all 3 conditions (check all 3 sets)
                    # place a queen at [r][c] in the board
                    # update the sets (add to the sets)
                    # backtrack
                    # undo -- make [r][c] a "." again
                    # remove from the sets
        # call backtrack on first row


        cols = set()
        posDiag = set()
        negDiag = set()

        # init board

        board = [["."] * n for i in range(n)] # creates n x n board init to "."

        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
        
        backtrack(0)
        return res