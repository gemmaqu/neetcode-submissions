class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*(len(t) +1)
        dp[0] = 1
        for c in s:
            for j in range(len(t), 0, -1):
                if t[j-1] == c:
                    dp[j] += dp[j-1]
        return dp[-1]