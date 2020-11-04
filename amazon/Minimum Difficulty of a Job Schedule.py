class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        
        
        dp = [ [float("inf")] * (len(jobDifficulty)   for _ in range(len(d)+1)]
        
        
        
        """
        
        n, inf = len(jobDifficulty), float('inf')
        dp = [[inf] * n + [0] for i in xrange(d + 1)]
        for d in xrange(1, d + 1):
            for i in xrange(n - d + 1):
                maxd = 0
                for j in xrange(i, n - d + 1):
                    maxd = max(maxd, jobDifficulty[j])
                    dp[d][i] = min(dp[d][i], maxd + dp[d - 1][j + 1])
        return dp[d][0] if dp[d][0] < inf else -1
    