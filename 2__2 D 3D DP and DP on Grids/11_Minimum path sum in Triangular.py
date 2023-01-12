class Solution:
    def solveMemo(self, i, j, dp, triangle):
        n = len(triangle)
        if (dp[i][j] != -1):
            return dp[i][j]
        if (i == n-1):
            return triangle[i][j]
        down = triangle[i][j]+self.solveMemo(i+1, j, dp, triangle)
        diagonal = triangle[i][j]+self.solveMemo(i+1, j+1, dp, triangle)
        dp[i][j] = min(down, diagonal)
        return dp[i][j]

    def tabulation(self, m, n, dp, triangle):
        n = len(triangle)
        for j in range(n):
            dp[m-1][j] = triangle[m-1][j]
        for i in range(m-2, -1, -1):
            for j in range(i, -1, -1):
                down = triangle[i][j]+dp[i+1][j]
                diagonal = triangle[i][j]+dp[i+1][j+1]
                dp[i][j] = min(down, diagonal)
        return dp[0][0]

    def spaceOptimization(self, m, n, prev, triangle):
        n = len(triangle)
        for j in range(n):
            prev[j] = triangle[m-1][j]
        for i in range(m-2, -1, -1):
            curr = [-1 for i in range(n)]
            for j in range(i, -1, -1):
                down = triangle[i][j]+prev[j]
                diagonal = triangle[i][j]+prev[j+1]
                curr[j] = min(down, diagonal)
            prev = curr
        return prev[0]

    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        dp = [[-1 for i in range(n)] for j in range(n)]
        # return self.solveMemo(0,0,dp,triangle)
        # return self.tabulation(n,n,dp,triangle)

        prev = [-1 for i in range(n)]
        return self.spaceOptimization(n, n, prev, triangle)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
n = len(triangle)
dp = [[-1 for i in range(n)] for j in range(n)]
prev = [-1 for i in range(n)]

ob = Solution()
print(ob.solveMemo(0, 0, dp, triangle))
print(ob.tabulation(n, n, dp, triangle))
print(ob.spaceOptimization(n, n, prev, triangle))
