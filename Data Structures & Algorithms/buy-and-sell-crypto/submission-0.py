class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        # price = future - prev (or R - L)
        max_price = float("-inf")
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                curr_price = prices[right] - prices[left]
                max_price = max(max_price, curr_price)
                right += 1
        return max(max_price, 0)