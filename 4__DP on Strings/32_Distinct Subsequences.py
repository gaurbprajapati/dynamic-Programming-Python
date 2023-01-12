class Solution:
    def memo(self, s, t, i, j, dp):
        if (j == 0):
            return 1
        if (i == 0):
            return 0
        if (dp[i][j] != -1):
            return dp[i][j]

        if (s[i-1] == t[j-1]):
            dp[i][j] = self.memo(s, t, i-1, j-1, dp) + \
                self.memo(s, t, i-1, j, dp)
        else:
            dp[i][j] = self.memo(s, t, i-1, j, dp)

        return dp[i][j]

    def tabulation(self, s, t, n, m):
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for j in range(1, m+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if (s[i-1] == t[j-1]):
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]

    def spaceOptimization(self, s, t, n, m):
        prev = [0 for i in range(m+1)]

        prev[0] = 1

        for i in range(1, n+1):
            for j in range(m, 0, -1):
                if (s[i-1] == t[j-1]):
                    prev[j] = prev[j-1]+prev[j]
                else:
                    prev[j] = prev[j]
            # prev=curr
        return prev[m]

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        print(self.memo(s, t, n, m, dp))
        print(self.tabulation(s, t, n, m))

        print(self.spaceOptimization(s, t, n, m))


s = "rabbbit"
t = "rabbit"
ob = Solution()
ob.numDistinct(s, t)
