class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*(len(prices) + 2)

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    dp[i] = max(dp[i], prices[j] - prices[i])
        return max(dp)