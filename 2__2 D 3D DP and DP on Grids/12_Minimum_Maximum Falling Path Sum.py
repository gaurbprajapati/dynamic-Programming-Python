class Solution:
    def Memo(self, i, j, n, matrix, dp):
        if(j < 0 or j >= n):
            return 1e9
        if(i == 0):
            return matrix[0][j]
        if(dp[i][j] != -1):
            return dp[i][j]
        up = matrix[i][j] + self.Memo(i-1, j, n, matrix, dp)
        leftDiagonal = matrix[i][j] + self.Memo(i-1, j-1, n, matrix, dp)
        rightDiagonal = matrix[i][j] + self.Memo(i-1, j+1, n, matrix, dp)
        dp[i][j] = min(up, leftDiagonal, rightDiagonal)
        return dp[i][j]

    def tabulation(self, m, n, matrix, dp):
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(0, n):
                up = matrix[i][j] + dp[i-1][j]
                leftDiagonal = matrix[i][j]
                if(j-1 >= 0):
                    leftDiagonal += dp[i-1][j-1]
                else:
                    leftDiagonal += 1e9

                rightDiagonal = matrix[i][j]
                if(j+1 < m):
                    rightDiagonal += dp[i-1][j+1]
                else:
                    rightDiagonal += 1e9
                dp[i][j] = min(up, min(leftDiagonal, rightDiagonal))

        ans = 1000000000000
        for i in range(n):
            ans = min(ans, dp[n-1][i])
        return ans

    def spaceOptimization(self, m, n, matrix, prev):
        for j in range(n):
            prev[j] = matrix[0][j]

        for i in range(1, m):
            curr = [-1 for i in range(n)]
            for j in range(n):
                up = matrix[i][j] + prev[j]
                leftDiagonal = matrix[i][j]
                if(j-1 >= 0):
                    leftDiagonal += prev[j-1]
                else:
                    leftDiagonal += 1e9

                rightDiagonal = matrix[i][j]
                if(j+1 < m):
                    rightDiagonal += prev[j+1]
                else:
                    rightDiagonal += 1e9
                curr[j] = min(up, min(leftDiagonal, rightDiagonal))
            prev = curr

        ans = 1e9
        for i in range(n):
            ans = min(ans, prev[i])
        return ans

    def minFallingPathSum(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1 for i in range(n)] for j in range(m)]

# for tabulation :-
        # return self.tabulation(m,n,matrix,dp)

# for SpaceOptimization
        prev = [-1 for i in range(n)]
        return self.spaceOptimization(m, n, matrix, prev)

# for Memo:---
        # ans=1e9
        # for j in range (n):
        #     val=self.Memo(m-1,j,n,matrix,dp)
        #     ans=min(ans,val)
        # return ans


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
m = len(matrix)
n = len(matrix[0])
dp = [[-1 for i in range(n)] for j in range(m)]

ob = Solution()
ans = 1e9
for j in range(n):
    val = ob.Memo(m-1, j, n, matrix, dp)
    ans = min(ans, val)
print("Memo Ans", ans)


print("tabulation ans ", ob.tabulation(m, n, matrix, dp))

# prev = [-1 for i in range(n)]
print("SpaceOptimization ans ", ob.minFallingPathSum(matrix))
