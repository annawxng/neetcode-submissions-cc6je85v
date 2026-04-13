class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # spiral is right, down, left, up
        res = []
        # intialize 4 pointers -- L R T B, L = 0, R = # cols, B = # rows, T = 0

        left = 0
        top = 0
        right = len(matrix[0]) # cols
        bot = len(matrix) # rows

       
        #initalize 0, 0
        r = 0
        c = 0 
        
        # while L < R and T < B
        while left < right and top < bot:
           # get every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bot):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bot): # im so confused why we need to add this
                break

            for i in range(right - 1, left - 1, -1): # wow this line is super tricky
                res.append(matrix[bot - 1][i])
            bot -= 1

            for i in range(bot - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1



        # while going in all these directions, add to ur ouput
        # loop from left to right (start in top left corner) until u hit R - 1, now shift T +=1
        # then loop from top to bottom until u hit B - 1, now shift  R -= 1
        # now go from right to left until u hit L, now shift B -= 1
        # now go from bottom to up until u hit T, now shift L += 1
        
        return res
