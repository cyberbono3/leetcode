class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
       
       
         Input: [7,1,5,3,6,4]
         
         -1
         +6
       
         min_price = float("-inf")
         max_profit = 0
         for p in prices:
            min_price = max(min_price, -p)
            max_profit = max(max_profit, min_price + p)
        

       
        """
        min_price = float("-inf")
        max_profit = 0
        for p in prices:
            min_price = max(min_price, -p)
            max_profit = max(max_profit, min_price + p)
        return max_profit
        