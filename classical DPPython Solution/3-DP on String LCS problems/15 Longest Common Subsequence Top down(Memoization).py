

def LCS(s1, s2, n, m):

    dp = [[-1]*(1001) for i in range(1001)]

    if (n == 0 or m == 0):
        return 0
    if dp[n][m] != -1:
        return dp[n][m]

    if (s1[n-1] == s2[m-1]):
        dp[n][m] = 1+LCS(s1, s2, n-1, m-1)

    else:
        dp[n][m] = max(LCS(s1, s2, n-1, m), LCS(s1, s2, n, m-1))

    return dp[n][m]


s1 = "abcdmky"

s2 = "abcwdzmky"

print(LCS(s1, s2, len(s1), len(s2)))
