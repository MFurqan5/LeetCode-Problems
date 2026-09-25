class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        NEG = -1
        
        # dp[i][j][c] = max score reaching (i,j) with exact cost c
        dp = [[[NEG] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Starting cell (0,0) has value 0 → cost 0, score 0
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j]
                score = v
                cost = 0 if v == 0 else 1
                
                for c in range(k + 1):
                    if c < cost:
                        continue
                    best = NEG
                    if i > 0 and dp[i - 1][j][c - cost] != NEG:
                        best = max(best, dp[i - 1][j][c - cost] + score)
                    if j > 0 and dp[i][j - 1][c - cost] != NEG:
                        best = max(best, dp[i][j - 1][c - cost] + score)
                    dp[i][j][c] = best
        
        ans = max(dp[m - 1][n - 1])
        return ans if ans != NEG else -1