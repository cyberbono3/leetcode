class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
                      
        1 0 1 0 0     0  0  0  0 0
        1 0 1 1 1     0  0  1  1 1
        1 1 1 1 1     0  1  1  2
        1 0 0 1 0
        
        
        
        
        
        
        
        
        """
        
        R, C = len(matrix), len(matrix[0])
        dp = [[0]*(C+1) for _ in range(R+1)]
        
        side = 0
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r-1][c-1]  == "1":
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    side = max(side, dp[r][c])
        return side**2