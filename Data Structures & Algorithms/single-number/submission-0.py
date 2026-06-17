class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # non empty array
        # find single one element that does not appear twice
        # just do xor on all of nums
        res = 0
        for num in nums:
            res ^= num
        return res
        