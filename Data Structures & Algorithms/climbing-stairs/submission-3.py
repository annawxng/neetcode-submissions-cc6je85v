class Solution:
    def climbStairs(self, n: int) -> int:
        #dp problem
        # init dp array [0]*n+1, dp[0] is basically dummy var
        # we want to loop through i in range(3, n+1):, since we know:
            # dp[1] = 1, dp[2] = 2, dp[3] = dp[2] + dp[1] = 2 + 1 = 3,so we start there
        

        # at the end, return dp[n]

        # handle base cases too

        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1): # n + 1 since it's exclusive
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        