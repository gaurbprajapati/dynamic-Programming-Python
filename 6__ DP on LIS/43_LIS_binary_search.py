class Solution:

    def lis_Binary_search(self, arr, n):
        dp = []
        dp.append(arr[0])
        ans = 1
        for ind in range(1, n):
            if (arr[ind] > dp[-1]):
                dp.append(arr[ind])
                ans += 1
            else:
                index = bisect.bisect_left(dp, arr[ind])
                dp[index] = arr[ind]

        return ans

    def lengthOfLIS(self, nums) -> int:
        n = len(nums)

        return self.lis_Binary_search(nums, n)
