
class Solution:
    def memo(self, ind, prices, buy, dp, fee):
        if ind == len(prices):
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]
        # profit=0

        if (buy == 0):  # buy the stock
            dp[ind][buy] = max(-prices[ind]-fee+self.memo(ind+1,
                               prices, 1, dp, fee), self.memo(ind+1, prices, 0, dp, fee))
        if (buy == 1):  # sell the stock
            dp[ind][buy] = max(prices[ind]+self.memo(ind+1,
                               prices, 0, dp, fee), self.memo(ind+1, prices, 1, dp, fee))

        return dp[ind][buy]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[-1 for i in range(3)] for j in range(len(prices)+1)]
        return self.memo(0, prices, 0, dp, fee)
