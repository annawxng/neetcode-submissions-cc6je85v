class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4]
        # while left < right
        # if right + left == target
        # res .append [left, right]
        # if right + left > target, right -= 1,
        # if right + left < target, left += 1
        res = []
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[right] + numbers[left] == target:
                # i thought it was 0-indexed array it should be 1 indexed array
                res.append(left + 1)
                res.append(right + 1)
                return res
            if numbers[right] + numbers[left] > target:
                right -= 1
            elif numbers[right] + numbers[left] < target:
                left += 1
        return res
