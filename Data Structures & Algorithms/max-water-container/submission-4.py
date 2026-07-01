class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # amount of water - calc the area between two bars
        # area -> width * min(height1, height2)


        # we want to take the max of this - calc for all the bars
        

        # i think we would jst want to try to keep track of max area as we go


        # lets do an example

        # Input: height = [1,7,2,5,4,7,9,6]

        # Output: 36

        # two ptrs, left and right


        # maxArea = 0


        # Input: height = [1,7,2,5,4,7,9,6]
        #                  L             R 
        #  calc area at each step, update maxArea, shrink inward (move the pointer with the shorter height inward)

        left = 0
        right = len(heights) - 1
        # init area 
        maxArea = (right - left) * min(heights[left], heights[right])

        while left != right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            currArea = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, currArea)
        return maxArea


        # Testing:
        # Input: height = [1,7,2,5,4,7,9,6]