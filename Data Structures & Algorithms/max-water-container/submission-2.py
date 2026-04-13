class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width * height
        # max height - from left to right = store the max of left and max of right
        # once u get the max of both, do min(left, right), get the diff of right - left index = width
        # return max_height * width
        max_area = 0
        left , right = 0, len(heights) - 1
        max_left = [0,0] # val, index
        max_right = [0,0] # use list instead of tuple since tuple is immutable
        while left < right:
            max_height = min(heights[left], heights[right])
            width = right - left # dont do +1 at the end
            # also we want current width of right - left, not the max_right / max_left indices
            
            max_area = max(max_area, max_height * width)
            # dont move both pointers, instead move the shorter one
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1 # it doesn't matter which one u move if they are the same height
        return max_area
        


