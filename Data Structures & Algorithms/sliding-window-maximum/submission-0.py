class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1, 1, 1, 1, 1, 4*, 5 ]    k = 6
        #                 ^ this is the max, cont shift to the right
        # deque - used to eliminate these values
        # can elim previous vlaues in our window
        # deque - always decreasing
        # [------,-, 5]  # 4 > deque, pop top of deque
        #                       [4, 5]  5 > top of deque (4)
        #                        ^ final output
        # O(n), O(1) -- add / remove is constant for deque
        # monotonically decreasing queue
       
        # deque instead of stack - we want to add / remove elements in beginning O(1) time, as well as end
         # [8, 7, 6, 9]       7 < 8, since we want max value, we want leftmost, and add 8 to output
         #      [-. -. 6, ]     9 > 6, so we pop the 6       output: [8, 7] 
         # [9] --> add to final output      output: [8, 7, 9] 
         output = []
         l = r = 0
         # deque
         # for r in range(nums)
         # pop smaller from back until u get >=
         # append r
         # remove out-of-window from front
         # if window size >= k, record max
         dq = collections.deque() # stores the indices
         while r < len(nums):
            # this guarantees monotonic decreasing
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if l > dq[0]:
                # dq[0] is oldest / max candidate index
                # l moves past it, it's no longer inside [l..r]
                dq.popleft()
            if (r + 1) >= k:
                output.append(nums[dq[0]]) # we want to append the max, which is the leftmost
                l += 1
            r += 1
         return output


#         left end              right end
# [   8 ,   6 ,   3   ]
#   ^                  ^
#  front               back
# popleft() removes 8
# pop() removes 3

