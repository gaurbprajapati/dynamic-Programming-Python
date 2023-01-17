class Solution:
    def memo(self, ind, prices, buy, dp, day):
        if ind == len(prices) or day == 0:
            return 0

        if dp[ind][buy][day] != -1:
            return dp[ind][buy][day]
        # profit=0

        if (buy == 0 and day > 0):  # buy the stock
            dp[ind][buy][day] = max(-prices[ind]+self.memo(ind+1, prices,
                                    1, dp, day), self.memo(ind+1, prices, 0, dp, day))
        if (buy == 1):  # sell the stock
            dp[ind][buy][day] = max(
                prices[ind]+self.memo(ind+1, prices, 0, dp, day-1), self.memo(ind+1, prices, 1, dp, day))

        return dp[ind][buy][day]

    def tabulation(self, n, prices, k):
        dp = [[[0 for i in range(k+1)] for j in range(2)]
              for k in range(len(prices)+1)]
        # dp[n][0] = dp[n][1]=0
        for ind in range(n-1, -1, -1):
            for buy in range(0, 2):
                for day in range(1, 3):
                    if (buy == 0):  # buy the stock
                        dp[ind][buy][day] = max(-prices[ind] +
                                                dp[ind+1][1][day], dp[ind+1][0][day])

                    if (buy == 1):  # sell the stock
                        dp[ind][buy][day] = max(
                            prices[ind]+dp[ind+1][0][day-1], dp[ind+1][1][day])
        return dp[0][0][2]

    def spaceOptimization(self, n, prices, k):
        after = [[0 for i in range(k+1)] for j in range(2)]
        curr = [[0 for i in range(k+1)] for j in range(2)]
        for ind in range(n-1, -1, -1):
            for buy in range(0, 2):
                for day in range(1, 3):
                    if (buy == 0):  # buy the stock
                        curr[buy][day] = max(-prices[ind] +
                                             after[1][day], after[0][day])

                    if (buy == 1):  # sell the stock
                        curr[buy][day] = max(
                            prices[ind]+after[0][day-1], after[1][day])
            after = curr
        return after[0][k]

    # using N*(k*2) array

    def memo_N_2K(self, ind, trans, prices, dp):
        if (ind == len(prices) or trans == 4):
            return 0

        if (dp[ind][trans] != -1):
            return dp[ind][trans]

        if (trans % 2 == 0):  # it is even --> buy the stock
            dp[ind][trans] = max(-prices[ind] + self.memo_N_2K(ind+1, trans+1,
                                 prices, dp), 0 + self.memo_N_2K(ind+1, trans, prices, dp))

        if (trans % 2 != 0):
            dp[ind][trans] = max(prices[ind] + self.memo_N_2K(ind+1, trans+1,
                                 prices, dp), 0 + self.memo_N_2K(ind+1, trans, prices, dp))

        return dp[ind][trans]

    def tabulation_N_2K(self, n, k, prices):
        dp = [[0 for i in range(4+1)] for j in range(len(prices)+1)]

        for ind in range(n-1, -1, -1):
            for trans in range(k*2-1, -1, -1):
                if (trans % 2 == 0):  # it is even --> buy the stock
                    dp[ind][trans] = max(-prices[ind] + dp[ind+1]
                                         [trans+1], 0 + dp[ind+1][trans])

                if (trans % 2 != 0):
                    dp[ind][trans] = max(
                        prices[ind] + dp[ind+1][trans+1], 0 + dp[ind+1][trans])

        return dp[0][0]
    # or---
#     def tabulation_N_2K(self,n,k,prices):
#         dp=[[0 for i in range (4+1)] for  j in range (len(prices)+1)]

#         for ind in range (n-1,-1,-1):
#             for trans in range (1,k*2+1):
#                 if (trans%2==0): #it is even --> buy the stock
#                     dp[ind][trans]= max( -prices[ind]+ dp[ind+1][trans-1] , 0+ dp[ind+1][trans] )

#                 if (trans%2!=0):
#                     dp[ind][trans]=max( prices[ind] + dp[ind+1][trans-1] , 0+ dp[ind+1][trans])

#         return dp[0][k*2]

    def maxProfit(self, prices) -> int:
        dp = [[[-1 for i in range(3)] for j in range(2)]
              for k in range(len(prices))]
        # return self.memo(0,prices,0,dp,2)
        # return self.tabulation(len(prices),prices)
        # return self.spaceOptimization(len(prices),prices,2)

        dp = [[-1 for i in range(4+1)] for j in range(len(prices))]
        # return self.memo_N_2K(0, 0,prices,dp)
        return self.tabulation_N_2K(len(prices), 2, prices)


prices = [3, 3, 5, 0, 0, 3, 1, 4]
ob = Solution()
print(ob.maxProfit(prices))
