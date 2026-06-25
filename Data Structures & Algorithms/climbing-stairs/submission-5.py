class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 2 3
        # we need 0th index

        # 0 1 2 3
        # 1 + 1 + 1 = 3
        # 1 + 2 = 3
        # 2 + 1
        # 1 2 
        # to get to 1, there is only one way
        # to get to 2, you can do: 1 + 1, or 2

        # base case

        # dp[1] = 1
        # dp[2] = 2
        # dp[i] = dp[i - 1] + dp[i - 2]
        dp = [0] * (n + 1) # last entry would be nth index
        if n == 1:
            return 1
        dp[1] =  1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]




