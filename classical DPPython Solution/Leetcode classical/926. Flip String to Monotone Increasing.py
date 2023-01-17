class Solution:
    def memo(self, s, ind, prev, dp):
        if ind >= len(s):
            return 0

        if dp[ind][prev] != -1:
            return dp[ind][prev]
        flip = 1000000
        notflip = 10000000
        ans = 10000000
        if (s[ind] == '0'):
            if (prev == 0):
                notflip = 0 + self.memo(s, ind+1, 0, dp)
                flip = 1 + self.memo(s, ind+1, 1, dp)
            else:
                flip = 1 + self.memo(s, ind+1, 1, dp)
        # s[ind]==1
        if (s[ind] == '1'):
            if (prev == 0):
                notflip = 0 + self.memo(s, ind+1, 1, dp)
                flip = 1 + self.memo(s, ind+1, 0, dp)
            else:
                notflip = 0 + self.memo(s, ind+1, 1, dp)
        dp[ind][prev] = min(flip, notflip)

        return dp[ind][prev]

    def tabulation(self, s, n, prev):
        dp = [[0 for i in range(3)] for j in range(len(s)+2)]
        for ind in range(len(s)-1, -1, -1):
            for prev in range(0, 2):
                flip = 1000000
                notflip = 10000000
                ans = 10000000
                if (s[ind] == '0'):
                    if (prev == 0):
                        notflip = 0 + dp[ind+1][0]
                        flip = 1 + dp[ind+1][1]
                    else:
                        flip = 1 + dp[ind+1][1]
                # s[ind]==1
                if (s[ind] == '1'):
                    if (prev == 0):
                        notflip = 0 + dp[ind+1][1]
                        flip = 1 + dp[ind+1][0]
                    else:
                        notflip = 0 + dp[ind+1][1]
                dp[ind][prev] = min(flip, notflip)
        return dp[0][0]

    def spaceOptimization(self, s, ind):
        curr = [0 for i in range(2+1)]
        ahead = [0 for j in range(2+1)]
        dp = [[0 for i in range(3)] for j in range(len(s)+2)]
        for ind in range(len(s)-1, -1, -1):
            for prev in range(0, 2):
                flip = 1000000
                notflip = 10000000
                ans = 10000000
                if (s[ind] == '0'):
                    if (prev == 0):
                        notflip = 0 + ahead[0]
                        flip = 1 + ahead[1]
                    else:
                        flip = 1 + ahead[1]
                # s[ind]==1
                if (s[ind] == '1'):
                    if (prev == 0):
                        notflip = 0 + ahead[1]
                        flip = 1 + ahead[0]
                    else:
                        notflip = 0 + ahead[1]
                curr[prev] = min(flip, notflip)
            ahead = curr

        return ahead[0]

    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [[-1 for i in range(2+1)] for j in range(len(s)+1)]
        return self.memo(s, 0, 0, dp)
        # return self.tabulation(s,len(s),0)
        # return self.spaceOptimization(s,len(s))
