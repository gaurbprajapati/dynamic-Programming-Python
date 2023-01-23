class Solution:
    def check(self, s1, s2, i=0, j=0):
        # a=0

        if len(s1)+1 != len(s2):
            return False

        while(j < len(s2)):
            if i < len(s1) and s1[i] == s2[j]:
                i += 1
                j += 1

            else:
                j += 1

        if i == len(s1) and len(s2):
            return True

        return False

    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        dp = [1 for i in range(len(words))]
        for ind in range(0, len(words)):
            for prev in range(0, ind):
                if (self.check(words[prev], words[ind])):
                    if (dp[prev]+1 > dp[ind]):
                        dp[ind] = 1+dp[prev]

        return max(dp)


words = ["a", "b", "ba", "bca", "bda", "bdca"]
# words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
words.sort(key=len)
ob = Solution()

print(words)
# print(ob.check(words[4], words[2]))
print(ob.longestStrChain(words))
