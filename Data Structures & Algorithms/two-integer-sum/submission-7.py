class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}
        for i, val in enumerate(nums):
            left = target - val
            if left in prevDict:
                return [prevDict[left], i]
            prevDict[val] = i
        return prevDict

            

        