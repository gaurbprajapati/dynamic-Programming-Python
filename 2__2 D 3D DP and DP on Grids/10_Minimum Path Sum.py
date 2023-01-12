
class Solution:
    def solveMemo(self, i, j, dp, grid):
        if (i == 0 and j == 0):
            return grid[i][j]
        if (i < 0 or j < 0):
            return 1e9
        if (dp[i][j] != -1):
            return dp[i][j]
        up = grid[i][j] + self.solveMemo(i-1, j, dp, grid)
        left = grid[i][j]+self.solveMemo(i, j-1, dp, grid)
        dp[i][j] = min(up, left)
        return dp[i][j]

    # def tabulation(self, m, n, dp,grid):
    #     dp[0][0]=grid[0][0]
    #     for j in range(1, n):
    #         dp[0][j]=dp[0][j-1]+grid[0][j]
    #     for i in range (1,m):
    #         dp[i][0]=dp[i-1][0]+grid[i][0]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
    #     return dp[m-1][n-1]
# '''OR tabulation  way 2 '''
    def tabulation(self, m, n, dp, grid):
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0):
                    dp[i][j] = grid[0][0]
                else:
                    if (i > 0):
                        up = grid[i][j]+dp[i-1][j]
                    else:
                        up = 1e9
                    if(j > 0):
                        left = grid[i][j]+dp[i][j-1]
                    else:
                        left = 1e9
                    dp[i][j] = min(up, left)
        return dp

    def spaceOptimization(self, m, n, prev, grid):
        for i in range(m):
            curr = [0 for i in range(n)]
            for j in range(n):
                if (i == 0 and j == 0):
                    curr[j] = grid[0][0]
                else:
                    up = grid[i][j]
                    if (i > 0):
                        up += prev[j]
                    else:
                        up += 1e9
                    left = grid[i][j]
                    if(j > 0):
                        left += curr[j-1]
                    else:
                        left += 1e9
                    curr[j] = min(up, left)
            prev = curr

        return prev[n-1]

    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        prev = [-1 for i in range(n)]
        return self.spaceOptimization(m, n, prev, grid)
        # return self.solveMemo(m-1,n-1,dp,grid)
        # return self.tabulation(m,n,dp,grid)


grid = [[1, 3, 9], [1, 5, 1], [4, 2, 1]]
m = len(grid)
n = len(grid[0])
dp = [[-1 for i in range(n)] for j in range(m)]
prev = [-1 for i in range(n)]

ob = Solution()
print(ob.solveMemo(m-1, n-1, dp, grid))
print(ob.tabulation(m, n, dp, grid))
print(ob.spaceOptimization(m, n, prev, grid))
