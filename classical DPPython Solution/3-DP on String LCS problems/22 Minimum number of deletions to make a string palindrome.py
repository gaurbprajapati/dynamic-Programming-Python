
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


def longestPalinSubseq(S):

    return LCS(S, S[::-1], len(S), len(S))


def minDeletions(Str, n):

    return n-longestPalinSubseq(Str)


n = 7
Str = "aebcbda"
print(longestPalinSubseq(Str))
