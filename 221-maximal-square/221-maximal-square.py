class Solution:
    def maximalSquare(self, M):
        m, n, ans = len(M), len(M[0]), 0
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i, j in product(range(m-1, -1, -1), range(n-1, -1, -1)):
            dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) if M[i][j] == '1' else 0
            ans = max(ans, dp[i][j])
        return ans * ans