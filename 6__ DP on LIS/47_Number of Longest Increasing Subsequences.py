from collections import Counter


class Solution:
    def printLis(self, arr, n):
        dp = [1 for i in range(n)]
        count = [1 for i in range(n)]
        for ind in range(n):
            for prev in range(0, ind):
                if (arr[prev] < arr[ind] and 1+dp[prev] > dp[ind]):
                    dp[ind] = 1+dp[prev]
                    count[ind] = count[prev]
                elif (arr[prev] < arr[ind] and 1+dp[prev] == dp[ind]):
                    count[ind] = count[prev]+count[ind]

        mx = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == mx:
                ans += count[i]

        return ans

    def findNumberOfLIS(self, nums) -> int:
        # if len(set(nums)) == 1:
        #     return len(nums)
        return self.printLis(nums, len(nums))


nums = [1, 2, 4, 3, 5, 4, 7, 2]
# nums = [1, 3, 5, 4, 7]
# nums = [2, 2, 2, 2, 2]
# nums = [3, 1, 2]

ob = Solution()

print(ob.findNumberOfLIS(nums))
