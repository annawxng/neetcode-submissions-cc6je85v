class Solution:
    def trap(self, height: List[int]) -> int:
        # at specific position i, amount of water that can be trapped is min of height(i-1, i +1)
         # if i + 1 has no black bar, or i - 1 has no black bar, then the height is just the other one
        # min(L,R) - height[i]
        left = 0
        # make sure to -1 for the right pointer
        right = len(height) - 1
        max_left = 0
        max_right = 0
        area = 0

        while left < right:
            # check heights before incrementing pointer
            if height[left] > height[right]:
                max_right = max(max_right, height[right])
                area += max(max_right - height[right], 0)
                right -= 1
            else:
                max_left = max(max_left, height[left])
                area += max(max_left - height[left], 0)
                left += 1
        return area