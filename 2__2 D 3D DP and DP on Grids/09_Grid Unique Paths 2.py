class Solution:
    def solveMemo(self, i, j, dp, obstacleGrid):
        if (i == 0 and j == 0):
            return 1
        if (i < 0 or j < 0):
            return 0
        if (obstacleGrid[i][j] == 1):
            return 0
        if (dp[i][j] != -1):
            return dp[i][j]
        up = self.solveMemo(i-1, j, dp, obstacleGrid)
        left = self.solveMemo(i, j-1, dp, obstacleGrid)
        dp[i][j] = up+left
        return dp[i][j]

    def tabulation(self, m, n, dp, obstacleGrid):
        for i in range(0, m):
            for j in range(0, n):
                up = 0
                left = 0
                if (obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                    continue
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

    def spaceOptimization(self, m, n, obstacleGrid, prev):
        for i in range(0, m):
            temp = [-1 for i in range(n)]
            for j in range(0, n):
                up = 0
                left = 0
                if (obstacleGrid[i][j] == 1):
                    temp[j] = 0
                    continue
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

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        dp = [[-1 for i in range(len(obstacleGrid[0]))]
              for j in range(len(obstacleGrid))]
        prev = [-1 for i in range(len(obstacleGrid[0]))]
        if obstacleGrid[0][0] == 1:
            return 0
        return self.spaceopimization(len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid, prev)
        # return self.tabulation(len(obstacleGrid),len(obstacleGrid[0]),dp,obstacleGrid)
        # return self.solveMemo(len(obstacleGrid)-1,len(obstacleGrid[0])-1,dp,obstacleGrid)


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
dp = [[-1 for i in range(len(obstacleGrid[0]))]
      for j in range(len(obstacleGrid))]
prev = [-1 for i in range(len(obstacleGrid[0]))]
m = len(obstacleGrid)
n = len(obstacleGrid[0])

ob = Solution()
print(ob.solveMemo(m-1, n-1, dp, obstacleGrid))
print(ob.tabulation(m, n, dp, obstacleGrid))
print(ob.spaceOptimization(m, n, obstacleGrid, prev))
