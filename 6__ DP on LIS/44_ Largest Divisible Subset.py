class Solution:
    def printLis(self, arr, n):

        dp = [1]*(n)
        hashm = [i for i in range(n)]

        for ind in range(0, n):
            hashm[ind] = ind
            for prev in range(ind):
                if (arr[ind] % arr[prev] == 0 and 1+dp[prev] > dp[ind]):
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

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        return self.printLis(nums, len(nums))
