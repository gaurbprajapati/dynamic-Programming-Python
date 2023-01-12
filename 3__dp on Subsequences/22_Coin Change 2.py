class Solution:
    def memo(self, coins, ind, t, dp):
        if ind == 0:
            if (t % coins[ind] == 0):
                return 1
            else:
                return 0
        if (dp[ind][t] != -1):
            return dp[ind][t]

        nottake = self.memo(coins, ind-1, t, dp)

        take = 0
        if (coins[ind] <= t):
            take = self.memo(coins, ind, t-coins[ind], dp)

        dp[ind][t] = take+nottake
        return dp[ind][t]

    def tabulation(self, coins, n, t):
        dp = [[0 for i in range(t+1)] for j in range(n+1)]
        for i in range(0, t+1):
            if (i % coins[0] == 0):
                dp[0][i] = 1
            else:
                dp[0][t] == 0

        for ind in range(1, n):
            for target in range(0, t+1):
                nottake = dp[ind-1][target]
                take = 0
                if (coins[ind] <= target):
                    take = dp[ind][target-coins[ind]]
                dp[ind][target] = (take+nottake)

        return dp[n-1][t]

    def spaceOptimization(self, coins, n, t):
        prev = [0 for i in range(t+1)]
        curr = [0]*(t+1)
        for i in range(0, t+1):
            if (i % coins[0] == 0):
                prev[i] = 1
            else:
                prev[i] = 0

        for ind in range(1, n):
            for target in range(0, t+1):
                nottake = prev[target]
                take = 0
                if (coins[ind] <= target):
                    take = curr[target-coins[ind]]

                curr[target] = (take+nottake)

            prev = curr

        return prev[t]

    def change(self, Sum: int, coins) -> int:
        n = len(coins)
        dp = [[-1 for i in range(Sum+1)] for j in range(n+1)]

        # return self.memo(coins,n-1,Sum,dp)

        # return self.tabulation(coins,n,Sum)

        return self.spaceOptimization(coins, n, Sum)


amount = 5
coins = [1, 2, 5]

ob = Solution()
print(ob.change(amount, coins))
