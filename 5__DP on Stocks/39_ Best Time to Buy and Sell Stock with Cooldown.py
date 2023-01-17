class Solution:
    def memo(self, ind, prices, buy, dp):
        if (ind >= len(prices)):
            return 0

        if (dp[ind][buy] != -1):
            return dp[ind][buy]

        if (buy == 1):  # buy stock
            dp[ind][buy] = max(-prices[ind] + self.memo(ind+1,
                               prices, 0, dp), 0 + self.memo(ind+1, prices, 1, dp))

        if (buy == 0):  # sell tock
            dp[ind][buy] = max(
                prices[ind]+self.memo(ind+2, prices, 1, dp), 0 + self.memo(ind+1, prices, 0, dp))
        return dp[ind][buy]

    def maxProfit(self, prices) -> int:

        dp = [[-1 for i in range(3)] for j in range(len(prices)+1)]

        return self.memo(0, prices, 1, dp)
