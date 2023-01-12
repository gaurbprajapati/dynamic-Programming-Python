
def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


def sequence_patter_matching(s1, s2):

    if len(s1) == LCS(s1, s2, len(s1), len(s2)):
        return True

    return False


s1 = "AXY"
s2 = "ADXCPY"

print(sequence_patter_matching(s1, s2))
