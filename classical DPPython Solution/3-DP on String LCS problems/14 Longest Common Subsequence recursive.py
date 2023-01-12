

def LCS(s1, s2, n, m):

    if (n == 0 or m == 0):
        return 0

    if (s1[n-1] == s2[m-1]):
        return 1+LCS(s1, s2, n-1, m-1)

    else:
        return max(LCS(s1, s2, n-1, m), LCS(s1, s2, n, m-1))


s1 = "abcdmky"

s2 = "abcwdzmky"

print(LCS(s1, s2, len(s1), len(s2)))
