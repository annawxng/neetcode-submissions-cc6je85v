class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1, 2, 3, 4, 5]
        # [2, 3, 4, 5, 1]
        # [4, 5, 1, 2, 3]
        # while left < right:

        # mid > right => left = mid + 1
        # mid < right ==> right = mid
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

        