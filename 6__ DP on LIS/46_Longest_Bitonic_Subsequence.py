# User function Template for python3

import bisect


class Solution:
    def lis(self, arr, n):
        dp = [1]*(n)

        for ind in range(0, n):
            for prev in range(ind):
                if (arr[prev] < arr[ind] and 1+dp[prev] > dp[ind]):
                    dp[ind] = 1+dp[prev]

        return dp

    def LongestBitonicSequence(self, nums):
        n = len(nums)
        r1 = self.lis(nums, n)
        r2 = self.lis(nums[::-1], n)[::-1]
        ans = 0
        for i in range(n):
            ans = max(ans, r1[i]+r2[i])
        return ans-1


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.LongestBitonicSequence(nums)
        print(ans)
# } Driver Code Ends
