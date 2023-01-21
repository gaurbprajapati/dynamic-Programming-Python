# https://practice.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1?

class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        return self.printLis(arr, N)

    def printLis(self, arr, n):

        dp = [1]*(n)
        hashm = [i for i in range(n)]

        for ind in range(0, n):
            hashm[ind] = ind
            for prev in range(ind):
                if (arr[prev] < arr[ind] and 1+dp[prev] > dp[ind]):
                    dp[ind] = 1+dp[prev]
                    hashm[ind] = prev
        lastind = -1
        lenLCS = -1
        for i in range(n):
            if (dp[i] > lenLCS):
                lastind = i
                lenLCS = dp[i]
        ans = []
        ans.append(arr[lastind])
        while(hashm[lastind] != lastind):
            lastind = hashm[lastind]
            ans.append(arr[lastind])

        return ans[::-1]


arr = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(arr)
ob = Solution()
print(ob.longestIncreasingSubsequence(n, arr))
