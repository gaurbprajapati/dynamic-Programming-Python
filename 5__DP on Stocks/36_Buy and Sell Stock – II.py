class Solution:
    def memo(self, ind, prices, buy, dp):
        if ind == len(prices):
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]
        # profit=0

        if (buy == 0):  # buy the stock
            dp[ind][buy] = max(-prices[ind]+self.memo(ind+1,
                               prices, 1, dp), self.memo(ind+1, prices, 0, dp))
        if (buy == 1):  # sell the stock
            dp[ind][buy] = max(prices[ind]+self.memo(ind+1,
                               prices, 0, dp), self.memo(ind+1, prices, 1, dp))

        return dp[ind][buy]

    def tabulation(self, n, prices):
        dp = [[0 for i in range(3)] for j in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for ind in range(n-1, -1, -1):
            for buy in range(0, 2):
                if (buy == 0):  # buy the stock
                    dp[ind][buy] = max(-prices[ind]+dp[ind+1][1], dp[ind+1][0])

                if (buy == 1):  # sell the stock
                    dp[ind][buy] = max(prices[ind]+dp[ind+1][0], dp[ind+1][1])
        return dp[0][0]

    def spaceOptimization(self, n, prices):
        prahead = [0 for i in range(3)]
        curr = [0 for i in range(3)]
        for ind in range(n-1, -1, -1):
            for buy in range(0, 2):
                if (buy == 0):  # buy the stock
                    curr[buy] = max(-prices[ind]+prahead[1], prahead[0])

                if (buy == 1):  # sell the stock
                    curr[buy] = max(prices[ind]+prahead[0], prahead[1])
                prahead = curr
        return prahead[0]

    # using N*4 array

    def maxProfit(self, prices) -> int:
        dp = [[-1 for i in range(2)] for j in range(len(prices))]
        # return self.memo(0,prices,0,dp)
        # return self.tabulation(len(prices),prices)
        return self.spaceOptimization(len(prices), prices)


prices = [7, 1, 5, 3, 6, 4]
ob = Solution()
print(ob.maxProfit(prices))
