class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetsumproblem(n, arr, sum):
            dp = [[False for i in range(sum + 1)] for i in range(n + 1)]
            for i in range(n+1):
                for j in range(sum+1):
                    if i == 0 and j == 0:
                        dp[i][j] = True
                    elif i == 0:
                        dp[i][j] = False
                    elif j == 0:
                        dp[i][j] = True

                    elif (arr[i-1] <= j):
                        dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])

                    elif (arr[i-1] > j):
                        dp[i][j] = dp[i-1][j]

            return dp[n][sum]

        s = sum(nums)
        if s % 2 != 0:
            return False
        return subsetsumproblem(len(nums), nums, s//2)
