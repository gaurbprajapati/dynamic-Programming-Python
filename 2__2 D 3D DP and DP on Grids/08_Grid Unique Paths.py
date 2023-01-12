# https://leetcode.com/problems/unique-paths/description/

class Solution:

    def solveMemo(self, i, j, dp):
        if (i == 0 and j == 0):
            return 1
        if (i < 0 or j < 0):
            return 0
        if (dp[i][j] != -1):
            return dp[i][j]
        up = self.solveMemo(i-1, j, dp)
        left = self.solveMemo(i, j-1, dp)
        dp[i][j] = up+left

        return dp[i][j]

    def tabulation(self, m, n, dp):
        for i in range(0, m):
            for j in range(0, n):
                up = 0
                left = 0
                if (i == 0 and j == 0):
                    dp[i][j] = 1
                    continue
                else:
                    if (i > 0):
                        up = dp[i-1][j]
                    if (j > 0):
                        left = dp[i][j-1]
                dp[i][j] = up+left
        return dp[m-1][n-1]

    def spaceOptimization(self, m, n, prev):
        for i in range(0, m):
            temp = [-1 for i in range(n)]
            for j in range(0, n):
                up = 0
                left = 0
                if (i == 0 and j == 0):
                    temp[j] = 1
                    continue
                else:
                    if (i > 0):
                        up = prev[j]
                    if (j > 0):
                        left = temp[j-1]
                temp[j] = up+left
            prev = temp

        return prev[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        # return self.solveMemo(m-1,n-1,dp)
        # return self. tabulation(m,n,dp)
        prev = [-1 for i in range(n)]
        return self.spaceOptimization(m, n, prev)


m = 3
n = 7
prev = [-1 for i in range(n)]
dp = [[-1 for i in range(n)] for j in range(m)]
ob = Solution()

print(ob.uniquePaths(m, n))
print(ob.solveMemo(m-1, n-1, dp))
print(ob.tabulation(m, n, dp))
