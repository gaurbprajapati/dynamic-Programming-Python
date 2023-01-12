# https://leetcode.com/problems/shortest-common-supersequence/description/

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
    return dp


def printing_SCS(s1, s2, n, m):
    dp = LCS(s1, s2, n, m)

    i = n
    j = m
    ans = ""
    while(i > 0 and j > 0):
        if (s1[i-1] == s2[j-1]):
            ans += s1[i-1]
            i -= 1
            j -= 1
        else:
            if (dp[i][j-1] > dp[i-1][j]):
                ans += s2[j-1]
                j -= 1
            else:
                ans += s1[i-1]
                i -= 1

    while(i > 0):
        ans += s1[i-1]
        i -= 1

    while(j > 0):
        ans += s2[j-1]
        j -= 1

    return ans


# X = "abac"
# Y = "cab"

X = "bbbaaaba"
Y = "bbababbb"

# X = "AGGTAB"
# Y = "GXTXAYB"
n = len(X)
m = len(Y)
print(printing_SCS(X, Y, n, m))
