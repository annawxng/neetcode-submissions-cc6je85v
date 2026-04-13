class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort input array
        # [-4, -1, -1, 0, 1, 2]
        # [ -4, ] => L R pointer for remaining elements to see if they add up to 0
            # if -4 + L + R == 0 ==> res.append([-4, L, R])
        
        # dupes - if current number is same as previous, then skip it (this will catch dup0es after u sorted the list)
        # O(nlogn)
        nums.sort()
        
        for i in range(len(nums)):
            curr_num = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if curr_num + nums[left] + nums[right] == 0:
                    res.append((curr_num, nums[left], nums[right]))
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif curr_num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res