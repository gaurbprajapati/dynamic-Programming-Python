class Solution:
    def memo(self, coins, ind, target, dp):
        if ind == 0:
            if (target % coins[ind] == 0):
                return target//coins[ind]
            else:
                return 1e9
        if (dp[ind][target] != -1):
            return dp[ind][target]
        nottake = 0+self.memo(coins, ind-1, target, dp)
        take = 1e9
        if(coins[ind] <= target):
            take = 1+self.memo(coins, ind, target-coins[ind], dp)
        dp[ind][target] = min(take, nottake)
        return dp[ind][target]

    def tabulation(self, coins, n, targets):
        dp = [[0]*(targets+1) for i in range(n+1)]
        for i in range(targets+1):
            if (i % coins[0] == 0):
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = 1e9
        for ind in range(1, n):
            for target in range(0, targets+1):
                nottake = 0+dp[ind-1][target]
                take = 1e9
                if(coins[ind] <= target):
                    take = 1+dp[ind][target-coins[ind]]
                dp[ind][target] = min(take, nottake)

        ans = dp[n-1][targets]
        if(ans >= 1e9):
            return -1
        return ans

    def spaceOptimization(self, coins, n, targets):
        prev = [0 for i in range(targets+1)]
        for i in range(0, targets+1):
            if (i % coins[0] == 0):
                prev[i] = i//coins[0]
            else:
                prev[i] = 1e9
        for ind in range(1, n):
            curr = [0 for i in range(targets+1)]
            for target in range(0, targets+1):
                nottake = 0+prev[target]
                take = 1e9
                if(coins[ind] <= target):
                    take = 1+curr[target-coins[ind]]
                curr[target] = min(take, nottake)
            prev = curr

        ans = prev[targets]
        if(ans >= 1e9):
            return -1
        return ans

    def coinChange(self, coins: List[int], Sum: int) -> int:
        n = len(coins)
        dp = [[-1]*(Sum+1) for i in range(n+1)]

        # memoans=self.memo(coins,n-1,Sum,dp)
        # if memoans==1e9:
        #     return -1
        # else:
        #     return memoans

        # return self.tabulation(coins,n,Sum)

        return self.spaceOptimization(coins, n, Sum)
