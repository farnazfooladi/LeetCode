class Solution:
    def maximalSquare(self, M):
        m, n, ans = len(M), len(M[0]), 0
        for i, j in product(range(m-1, -1, -1), range(n-1, -1, -1)):
            if i == m-1 or j == n-1:
                M[i][j] = int(M[i][j])
                ans = max(ans, M[i][j])
            else:
                M[i][j] = 1 + min(M[i+1][j], M[i][j+1], M[i+1][j+1]) if M[i][j] == '1' else 0
                ans = max(ans, M[i][j])
        return ans * ans