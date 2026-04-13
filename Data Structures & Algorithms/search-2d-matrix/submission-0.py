class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

           # so, rows go like this
        # col 0 1 2 3 4
        # row 0
        # row 1 
        # row 2

        # two binary search
        # first binary seaerch - determine which row
        # top, bottom, mid
        # if target < first num of mid: bottom == mid - 1
        # elif target > last num of mid: top = mid + 1
        # elif target >= first num of mid && <= last num of mid:
            # u found ur target row, start binary search 2
            # break
        # if top > bottom: return False // target not in any row
        top = 0
        bottom = len(matrix) - 1
        target_row = -1
        cols_idx = len(matrix[0]) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][cols_idx]:
                target_row = mid
                break
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][cols_idx]:
                top = mid + 1
            if top > bottom:
                return False

        # 2nd binary search - dtermine which value inside of that row
        # regular binary search within that row - if u found ur value, then return true

        # at the very end, if u didn't find ur value, return false
        left = 0
        right = cols_idx
        while left <= right:
            middle = (left + right) // 2
            if target == matrix[target_row][middle]:
                return True
            if target < matrix[target_row][middle]:
                right = middle - 1
            else: # target > 
                left = middle + 1
        return False
