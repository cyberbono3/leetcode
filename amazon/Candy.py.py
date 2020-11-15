class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        
        [1, 2, 3]  
        
         1  2  3
         
         
         [1, 3, 2]
         
          1  2  1
          
          
          
        [1,2,87,87,87,2,1]
         1 2  3  1  3 2 1
        
        scan fro mleft to right andschecking if current element greater than previous one
             dp[i] = dp[i-1] + 1
        scan from right to elft if current element is greater than next element 
        
        output = 10
        expected = 13
         
        
    
        """
        
        n = len(ratings)
        
        
        dp = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
            
            
        for i in range(n-2, -1, -1):
            if dp[i] > dp[i+1]:
                dp[i] = dp[i+1] + 1
        return sum(dp)
            
    