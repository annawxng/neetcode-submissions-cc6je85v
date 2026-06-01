class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mp: value, idx
        mp = defaultdict(list)
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in mp:
                if idx < mp[diff]:
                    return [idx, mp[diff]]
                else:
                    return [mp[diff], idx]
            else:
                mp[num] = idx
        return -1