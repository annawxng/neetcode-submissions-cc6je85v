class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mp: value, idx
        mp = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in mp:
                return [mp[diff], idx]
            mp[num] = idx
        return []