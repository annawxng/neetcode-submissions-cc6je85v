class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost -> cost[i]
         # cost o ftaking step from ith floor of staircase
         # after paying cost[i], u can step into [i+1], or [i+2]
         # can start at index 0 or 1
         # return minimum cost to reach past last index


        # cost = [1,2,1,2,1,1,1]

        # i have no idea how to do this

        # dp[i] = min(opt_from_step_before, opt_from_two_steps_before)


        n = len(cost) # we want to reach 1 past the last index, not the last index

        dp = [0] * (n + 1) # we need n + 1 elements so we can access dp[n], which is min cost to reach the "top"

        for i in range(2, n + 1): # loop from 2 to n, since n + 1 is exclusive
            dp[i] = min(dp[i - 1] + cost[i-1],dp[i - 2] + cost[i-2])
        
        return dp[n]





