class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        
        
        k = 2, prices = 
        
             1   2   3  4  5   6   7
             10, 20, 60, 90, 15, 20
          1  0   10  40  80  80  80
          2  0   10  50
 
         
                 



        """
        dp = [ [0]*len(prices) for _ in range(k+1)]
           
        for i in range(1, k+1):
            for j in range(1, len(prices)):
                k_trans_profit = max(dp[i][m] + prices[j] - prices[m] for m in range(j))
                dp[i][j] = max(dp[i][j-1], k_trans_profit)
        
        return dp[-1][-1]
                   
                 