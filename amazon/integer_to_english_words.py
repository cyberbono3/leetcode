class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        
        
    
                
                
            

        """
        to10  = ["One","two","three","four", "five", "six", "seven", "eight", "nine"]
        
        to19 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "feefteen", "sixteen", "seventeen", "eighteen", "nineteen"]
                         
        tens = ["twenty", "thirty", "fourty", "fifty","sixty","seventy", "eighty", "ninety"]
        
        def words(n):
            
            if n < 10: 
                res.append(to10[n-1])
                return 
            
            if n < 20: 
                res.append(to19[n % 10])
                return 
                
            if n < 100:
                res.append(tens[n//10-2])
                words(n % 10)
                return
                
                                  
            for w, i in (("Bullion", pow(10, 9)), ("Million", pow(10, 6)), ("Thousand", 1000), ("Hundred", 100)):
                if n // i:
                    words(n//i) 
                    res.append(w) 
                    words(n % i)
        if not num:
            return "zero"
        res = []
        words(num)
        return " ".join(res)
                