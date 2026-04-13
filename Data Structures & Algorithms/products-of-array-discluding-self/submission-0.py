class Solution:
    # [1,2,4,6]
    # [1,1,2,8]  pref: 1
    # [24,24,12,8]  suff: 24


    # [-1,0,1,2,3] pref: -1
    # [1,1,1,1,1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = 1
        suffix_prod = 1
        n = len(nums)
        res = [1] * n
        for i in range(len(nums)):
            if i == 0:
                prefix_prod *= nums[i]
                continue
            res[i] = prefix_prod
            prefix_prod *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
        # n - 1 is the last index
        # -1 is the stop (exclusive, so it stops at 0)
        # -1 is the step (walk backward)
            if i == len(nums) - 1:
                suffix_prod *= nums[i]
                continue
            res[i] *= suffix_prod
            suffix_prod *= nums[i]
        return res



                        