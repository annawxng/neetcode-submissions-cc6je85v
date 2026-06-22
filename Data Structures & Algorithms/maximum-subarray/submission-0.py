class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set max_sum, curr_sum = nums[0] / initial element

        # loop from nums[1] until end of nums:
            # is extend or start fresh better?
            # update max_sum
        
        # return max_sum
        #  nums=[2,-3,4,-2,2,1,-1,4]

        # max_sum = 2
        # curr_sum = 2
        # extend = 2 + (-3) = -1
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            extend = curr_sum + nums[i]
            if nums[i] > extend:
                curr_sum = nums[i]
            else:
                curr_sum = extend
            max_sum = max(max_sum, curr_sum)
        return max_sum