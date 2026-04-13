class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mp:
                res.append(mp[diff])
                res.append(i)
                return res
            mp[num] = i
        return res
            